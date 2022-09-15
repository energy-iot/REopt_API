# *********************************************************************************
# REopt, Copyright (c) 2019-2020, Alliance for Sustainable Energy, LLC.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list
# of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice, this
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#
# Neither the name of the copyright holder nor the names of its contributors may be
# used to endorse or promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
# *********************************************************************************
import json
import sys
import uuid
import numpy as np

from celery import shared_task
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.bundle import Bundle
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.validation import Validation
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

from reo.exceptions import SaveToDatabase, UnexpectedError, REoptFailedToStartError

from reo.models import ScenarioModel, FinancialModel
from job.models import APIMeta, GeneratorOutputs, ElectricStorageInputs, ElectricStorageOutputs, PVOutputs, ElectricLoadInputs#, CHPOutputs
from resilience_stats.models import ResilienceModel, ERPMeta, ERPInputs, ERPOutputs, get_erp_input_dict_from_run_uuid
from resilience_stats.validators import validate_run_uuid
from resilience_stats.views import run_outage_sim


# POST data:{"run_uuid": UUID, "bau": True}


class ERPJob(ModelResource):

    class Meta:
        resource_name = 'erp'
        allowed_methods = ['post']
        detail_allowed_methods = []
        authorization = ReadOnlyAuthorization()
        serializer = Serializer(formats=['json'])
        always_return_data = True
        validation = Validation()
        object_class = None
        
    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.id
        else:
            kwargs['pk'] = bundle_or_obj['id']

        return kwargs

    def get_object_list(self, request):
        return [request]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)

    def obj_create(self, bundle, **kwargs):
        erp_run_uuid = str(uuid.uuid4())

        meta = {
            "run_uuid": erp_run_uuid,
            "reopt_version": "0.18.0",
            "status": "validating..." #TODO replace
        }
        if bundle.request.META.get('HTTP_X_API_USER_ID', False):
            if bundle.request.META.get('HTTP_X_API_USER_ID', '') == '6f09c972-8414-469b-b3e8-a78398874103':
                meta["job_type"] = 'REopt Web Tool'
            else:
                meta["job_type"] = 'developer.nrel.gov'
        else:
            meta["job_type"] = 'Internal NREL'
        test_case = bundle.request.META.get('HTTP_USER_AGENT','')
        if test_case.startswith('check_http/'):
            meta["job_type"] = 'Monitoring'
        meta = ERPMeta.create(**meta).save()

        reopt_run_uuid = bundle.data.get("reopt_run_uuid", None)
        try:
            validate_run_uuid(reopt_run_uuid)
        except ValidationError as err:
            raise ImmediateHttpResponse(HttpResponse(json.dumps({"Error": str(err.message)}), status=400))

        if reopt_run_uuid is not None:
            # Get inputs from a REopt run in database
            try:
                reopt_run_meta = APIMeta.objects.select_related(
                    "ElectricLoadOutputs",
                ).get(run_uuid=reopt_run_uuid)
                
            except:
                # Handle non-existent REopt runs
                msg = "Invalid run_uuid {}, REopt run does not exist.".format(reopt_run_uuid)
                raise ImmediateHttpResponse(HttpResponse(json.dumps({"Error": msg}), content_type='application/json', status=404))
            
            #TODO: put all of this stuff below in a helper function, or in clean or save django methods?
            critical_loads_kw = reopt_run_meta.ElectricLoadOutputs.dict["critical_load_series_kw"]
            # Have to try for CHP, PV, and Storage models because may not exist
            try: 
                chp_size_kw = get(reopt_run_meta.CHPOutputs.dict, "size_kw", 0)
            except: pass
            try:
                pvs = reopt_run_meta.PVInputs.all()
                pv_size_kw = 0
                pv_kw_series = np.zeros(len(critical_loads_kw))
                for pv in pvs:
                    pvd = pv.dict
                    pv_size_kw += pv
                    pv_kw_series += (
                        pvd.get("year_one_to_battery_series_kw", np.zeros(len(critical_loads_kw)))
                        + pvd.get("year_one_curtailed_production_series_kw", np.zeros(len(critical_loads_kw)))
                        + pvd.get("year_one_to_load_series_kw", np.zeros(len(critical_loads_kw)))
                        + pvd.get("year_one_to_grid_series_kw", np.zeros(len(critical_loads_kw)))
                    )
                pv_production_factor_series = pv_kw_series ./ pv_size_kw
            except: pass
            try:
                stor_out = reopt_run_meta.ElectricStorageOutputs.dict
                stor_in = reopt_run_meta.ElectricStorageInputs.dict
                battery_charge_efficiency = stor_in["rectifier_efficiency_pct"] * stor_in["internal_efficiency_pct"]**0.5
                battery_discharge_efficiency = stor_in["inverter_efficiency_pct"] * stor_in["internal_efficiency_pct"]**0.5
                battery_size_kwh = stor_out.get("size_kwh", 0)
                battery_size_kw = stor_out.get("size_kw", 0)
                init_soc = stor_out.get("year_one_soc_series_pct", [])
                starting_battery_soc_kwh = init_soc .* battery_size_kwh
            except: pass
            #TODO: figure out which way it should be
            # way 1: if the user provides a reopt run and a generator_size_kw to override that, num_generators defaults to 1
            try:
                gen = reopt_run_meta.GeneratorOutputs.dict
                if bundle.data.get("num_generators", None) is not None:
                    generator_size_kw = gen.get("size_kw", 0) / bundle.data["num_generators"])
                else:
                    generator_size_kw = gen.get("size_kw", 0)
            except: pass

            for field_name in ["critical_loads_kw", "battery_charge_efficiency",
                                "battery_discharge_efficiency", "battery_size_kw",
                                "battery_size_kwh", "starting_battery_soc_kwh",
                                "chp_size_kw", "generator_size_kw",
                                "pv_size_kw", "pv_production_factor_series"]:
                if bundle.data.get(field_name, None) is None:
                    try: bundle.data[field_name] = eval(field_name)
                    except: pass # if field_name variable wasn't set due to tech not being present then don't update
                
            # # way 2: if the user provides a reopt run and a generator_size_kw to override that, num_generators defaults to reopt results gen size divided by generator_size_kw
            # if bundle.data.get("num_generators", None) is None and bundle.data.get("generator_size_kw", None) is not None:
            #     try:
            #         gen = reopt_run_meta.GeneratorOutputs.dict
            #         bundle.data["num_generators"] = ceil(gen.get("size_kw", 0) / bundle.data["generator_size_kw"])
            #     except: bundle.data["num_generators"] = 1
            # else if bundle.data.get("num_generators", None) is not None and bundle.data.get("generator_size_kw", None) is None:
            #     try:
            #         gen = reopt_run_meta.GeneratorOutputs.dict
            #         bundle.data["generator_size_kw"] = gen.get("size_kw", 0) / bundle.data["num_generators"])
            #     except: pass #will error later when creating ERPInputs and ImmediateHttpResponse will be raised
            # else if bundle.data.get("num_generators", None) is None and bundle.data.get("generator_size_kw", None) is None:
            #     try:
            #         gen = reopt_run_meta.GeneratorOutputs.dict
            #         bundle.data["num_generators"] = 1
            #         bundle.data["generator_size_kw"] = gen.get("size_kw", 0)
            #     except: pass #will error later when creating ERPInputs and ImmediateHttpResponse will be raised

        try:
            erpinputs = ERPInputs.create(**bundle.data)
            erpinputs.clean_fields()
            # erpinputs.clean()
            erpinputs.save()

            run_erp_task.delay(erp_run_uuid)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise ImmediateHttpResponse(HttpResponse(json.dumps({"error": exc_value}),
                                        content_type='application/json',
                                        status=500))  # internal server error

        raise ImmediateHttpResponse(HttpResponse(json.dumps({'run_uuid': erp_run_uuid}),
                                    content_type='application/json', status=201))


class OutageSimJob(ModelResource):
    class Meta:
        resource_name = 'outagesimjob'
        allowed_methods = ['post']
        detail_allowed_methods = []
        authorization = ReadOnlyAuthorization()
        serializer = Serializer(formats=['json'])
        always_return_data = True
        validation = Validation()
        object_class = None

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            # Primary key is set to be the run_uuid for 1 to1 matching
            # between scenario UUID and outage sim UUID
            kwargs['pk'] = bundle_or_obj.data["run_uuid"]  # bundle_or_obj.obj.id
        else:
            kwargs['pk'] = bundle_or_obj.get("id")

        return kwargs

    def get_object_list(self, request):
        return [request]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)

    def obj_create(self, bundle, **kwargs):
        run_uuid = bundle.data.get("run_uuid")
        bau = bundle.data.get("bau", False)
        # Handle invalid uuids
        try:
            validate_run_uuid(run_uuid)
        except ValidationError as err:
            raise ImmediateHttpResponse(HttpResponse(json.dumps({"Error": str(err.message)}), status=400))

        # Handle non-existent scenario runs
        try:
            scenario = ScenarioModel.objects.get(run_uuid=run_uuid)
        except ScenarioModel.DoesNotExist:
            msg = "Scenario {} does not exist!.".format(run_uuid)
            raise ImmediateHttpResponse(HttpResponse(json.dumps({"Error": msg}), content_type='application/json', status=404))

        if scenario.status == "Optimizing...":
            raise ImmediateHttpResponse(HttpResponse(json.dumps({"Error": "The scenario is still optimizing. Please try again later."}),
                                content_type='application/json', status=500))
        elif "error" in scenario.status.lower():
            raise ImmediateHttpResponse(HttpResponse(json.dumps(
                {"Error": "An error occurred in the scenario. Please check the messages from your results."}),
                content_type='application/json', status=500))

        if ResilienceModel.objects.filter(scenariomodel=scenario).count() > 0:
            err_msg = ("An outage simulation job has already been created for this run_uuid."
                "Please retrieve the results with a GET request to v1/outagesimjob/<run_uuid>/results."
                " Note: Even if not specified when the job was created, business-as-usual (BAU) can be retrieved"
                " from the results endpoint by specifying bau=true in the URL parameters.")

            raise ImmediateHttpResponse(HttpResponse(
                json.dumps({"Warning": err_msg}),
                content_type='application/json',
                status=208))
        else:  # This is the first POST for this run_uuid, kick-off outage sim run
            try:
                rm = ResilienceModel.create(scenariomodel=scenario)
            except SaveToDatabase as e:
                raise ImmediateHttpResponse(
                HttpResponse(json.dumps({"Error": e.message}), content_type='application/json', status=500))
            run_outage_sim_task.delay(rm.scenariomodel_id, run_uuid, bau)
            bundle.data = {"run_uuid": run_uuid, "bau": bau, "Success": True, "Status": 201}

        return bundle

@shared_task
def run_erp_task(run_uuid):
    name = 'run_erp_task'
    data = get_erp_input_dict_from_run_uuid(run_uuid)

    user_uuid = data.get('user_uuid')
    data.pop('user_uuid',None) # Remove user uuid from inputs dict to avoid downstream errors

    logger.info("Running ERP tool ...")
    try:
        julia_host = os.environ.get('JULIA_HOST', "julia")
        response = requests.post("http://" + julia_host + ":8081/erp/", json=data)
        response_json = response.json()
        if response.status_code == 500:
            raise REoptFailedToStartError(task=name, message=response_json["error"], run_uuid=run_uuid, user_uuid=user_uuid)

    except Exception as e:
        if isinstance(e, REoptFailedToStartError):
            raise e

        if isinstance(e, requests.exceptions.ConnectionError):  # Julia server down
            raise REoptFailedToStartError(task=name, message="Julia server is down.", run_uuid=run_uuid, user_uuid=user_uuid)

        exc_type, exc_value, exc_traceback = sys.exc_info()
        logger.error("ERP raised an unexpected error: UUID: " + str(run_uuid))
        raise UnexpectedError(exc_type, exc_value, traceback.format_tb(exc_traceback), task=name, run_uuid=run_uuid,
                              user_uuid=user_uuid)
    else:
        logger.info("ERP run successful.")

    process_erp_results(response_json, run_uuid)
    return True

def process_erp_results(results: dict, run_uuid: str) -> None:
    """
    Saves ERP results returned from the Julia API in the backend database.
    Called in resilience_stats/run_erp_task (a celery task)
    """

    meta = ERPMeta.objects.get(run_uuid=run_uuid)
    # meta.status = results.get("status")
    # meta.save(update_fields=["status"])
    ERPOutputs.create(meta=meta, **results).save()
    

@shared_task
def run_outage_sim_task(scenariomodel_id, run_uuid, bau):

    results = run_outage_sim(run_uuid, with_tech=True, bau=bau)

    try:
        ResilienceModel.objects.filter(scenariomodel_id=scenariomodel_id).update(**results)
        results = {'avoided_outage_costs_us_dollars': results['avoided_outage_costs_us_dollars']}
        FinancialModel.objects.filter(run_uuid=run_uuid).update(**results)        
    except SaveToDatabase as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = SaveToDatabase(exc_type, exc_value.args[0], exc_traceback, task='resilience_model', run_uuid=run_uuid)
        err.save_to_db()
