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
import os
from tastypie.test import ResourceTestCaseMixin
from django.test import TestCase
import numpy as np


class ERPTests(ResourceTestCaseMixin, TestCase):
    REopt_tol = 1e-2

    def setUp(self):
        super(ERPTests, self).setUp()

        #for ERP simulation
        self.reopt_base_erp = '/dev/erp/'
        self.reopt_base_erp_results = '/dev/erp/{}/results/'
        self.reopt_base_erp_help = '/dev/erp/help/'
        self.reopt_base_erp_chp_defaults = '/dev/erp/chp_defaults/?prime_mover={0}&is_chp={1}&size_kw={2}'
        self.post_sim = os.path.join('resilience_stats', 'tests', 'ERP_sim_post.json')
        self.post_sim_large_stor = os.path.join('resilience_stats', 'tests', 'ERP_sim_large_stor_post.json')
        self.post_sim_only = os.path.join('resilience_stats', 'tests', 'ERP_sim_only_post.json')
        self.post_sim_long_dur_stor = os.path.join('resilience_stats', 'tests', 'ERP_sim_long_dur_stor_post')
        #for REopt optimization
        self.reopt_base_opt = '/dev/job/'
        self.reopt_base_opt_results = '/dev/job/{}/results'
        self.post_opt = os.path.join('resilience_stats', 'tests', 'ERP_opt_post.json')
        self.post_opt_long_dur_stor = os.path.join('resilience_stats', 'tests', 'ERP_opt_long_dur_stor_post')

    def get_response_opt(self, data):
        return self.api_client.post(self.reopt_base_opt, format='json', data=data)
    
    def get_results_opt(self, run_uuid):
        return self.api_client.get(self.reopt_base_opt_results.format(run_uuid))

    def get_response_sim(self, data_sim):
        return self.api_client.post(self.reopt_base_erp, format='json', data=data_sim)

    def get_results_sim(self, run_uuid):
        return self.api_client.get(self.reopt_base_erp_results.format(run_uuid))

    def get_help(self):
        return self.api_client.get(self.reopt_base_erp_help)
    
    def get_chp_defaults(self, prime_mover, is_chp, size_kw):
        return self.api_client.get(
            self.reopt_base_erp_chp_defaults.format(prime_mover, is_chp, size_kw),
            format='json'
        )

    def test_erp_long_duration_battery(self):
        post_opt = json.load(open(self.post_opt_long_dur_stor, 'rb'))
        resp = self.get_response_opt(post_opt)
        self.assertHttpCreated(resp)
        r_opt = json.loads(resp.content)
        reopt_run_uuid = r_opt.get('run_uuid')
        assert(reopt_run_uuid is not None)
        resp = self.get_results_opt(reopt_run_uuid)
        results_opt = json.loads(resp.content)["outputs"]

        post_sim = json.load(open(self.post_sim_long_dur_stor, 'rb'))
        resp = self.get_response_sim(post_sim)
        self.assertHttpCreated(resp)
        r_sim = json.loads(resp.content)
        erp_run_uuid = r_sim.get('run_uuid')
        resp = self.get_results_sim(erp_run_uuid)
        results_sim = json.loads(resp.content)["outputs"]

        expected_result = ([1]*79)+[0.999543,0.994178,0.9871,0.97774,0.965753,0.949429,0.926712,0.899543,0.863584,0.826712,0.785616,0.736416,0.683105,0.626256,0.571005,0.519064,0.47226,0.429909,0.391553,0.357306,0]
        #TODO: resolve bug where unlimted fuel markov portion of results goes to zero 1 timestep early
        for i in range(99):#min(length(simresults["probs_of_surviving"]), reliability_inputs["max_outage_duration"])
            self.assertAlmostEqual(results_sim["mean_cumulative_survival_by_duration"][i], expected_result[i], places=4)
        
    # def test_erp_large_battery(self):
    #     """
    #     Tests calling ERP with PV, a small generator, and very large battery such that final survivial should be 1.
    #     This is the same as the first test in the "Backup Generator Reliability" testset in the REopt Julia package.
    #     """
    #     post_sim_large_stor = json.load(open(self.post_sim_large_stor, 'rb'))

    #     resp = self.get_response_sim(post_sim_large_stor)
    #     self.assertHttpCreated(resp)
    #     r_sim = json.loads(resp.content)
    #     erp_run_uuid = r_sim.get('run_uuid')

    #     resp = self.get_results_sim(erp_run_uuid)
    #     results = json.loads(resp.content)

    #     self.assertAlmostEqual(results["outputs"]["mean_cumulative_survival_final_time_step"], 1.0, places=4)

    # def test_erp_with_reopt_run_uuid(self):
    #     """
    #     Tests calling ERP with a REopt run_uuid provided, but all inputs from REopt results overrided.
    #     This ends up being the same as the second to last test in the "Backup Generator Reliability" testset in the REopt Julia package.
    #     Then tests calling ERP with the same REopt run_uuid provided, but only the necessary additional ERP inputs provided.
    #     This used to be the same as the last test in the "Backup Generator Reliability" testset in the REopt Julia package, but need to make consistent again.
    #     """

    #     data = json.load(open(self.post_opt, 'rb'))
    #     resp = self.get_response_opt(data)
    #     self.assertHttpCreated(resp)
    #     r_opt = json.loads(resp.content)
    #     reopt_run_uuid = r_opt.get('run_uuid')

    #     assert(reopt_run_uuid is not None)
    #     post_sim = json.load(open(self.post_sim, 'rb'))
    #     post_sim["reopt_run_uuid"] = reopt_run_uuid
    #     post_sim["ElectricStorage"]["starting_soc_series_fraction"] = 8760 * [1]

    #     resp = self.get_response_sim(post_sim)
    #     self.assertHttpCreated(resp)
    #     r_sim = json.loads(resp.content)
    #     erp_run_uuid = r_sim.get('run_uuid')

    #     resp = self.get_results_sim(erp_run_uuid)
    #     results = json.loads(resp.content)
    #     self.assertAlmostEqual(results["outputs"]["unlimited_fuel_cumulative_survival_final_time_step"][0], 0.858756, places=4)
    #     self.assertAlmostEqual(results["outputs"]["cumulative_survival_final_time_step"][0], 0.858756, places=4)
    #     self.assertAlmostEqual(results["outputs"]["mean_cumulative_survival_final_time_step"], 0.904242, places=4)

    #     #remove inputs that override REopt results and run again
    #     for model, field in [
    #                 ("Generator","size_kw"),
    #                 ("PrimeGenerator","size_kw"),
    #                 ("ElectricStorage","size_kw"),
    #                 ("ElectricStorage","size_kwh"),
    #                 ("ElectricStorage","charge_efficiency"),
    #                 ("ElectricStorage","discharge_efficiency"),
    #                 ("ElectricStorage","starting_soc_series_fraction"),
    #                 ("PV","size_kw"),
    #                 ("PV","production_factor_series"),
    #                 ("Outage","critical_loads_kw"),
    #                 ("Outage","max_outage_duration")
    #             ]:
    #         post_sim.get(model,{}).pop(field, None)

    #     # add minimum_soc_fraction input to be consistent with test in REopt.jl
    #     post_sim["ElectricStorage"]["minimum_soc_fraction"] = 0.2
        
    #     resp = self.get_response_sim(post_sim)
    #     self.assertHttpCreated(resp)
    #     r_sim = json.loads(resp.content)
    #     erp_run_uuid = r_sim.get('run_uuid')

    #     resp = self.get_results_sim(erp_run_uuid)
    #     results = json.loads(resp.content)
    #     self.assertAlmostEqual(results["outputs"]["mean_cumulative_survival_by_duration"][23], 0.965763, places=4)
    #     self.assertAlmostEqual(results["outputs"]["cumulative_survival_final_time_step"][0], 0.962327, places=4)
    #     self.assertAlmostEqual(results["outputs"]["mean_cumulative_survival_final_time_step"], 0.965763, places=3)

    # def test_erp_with_no_opt(self):
    #     """
    #     Tests calling ERP on it's own without providing a REopt run_uuid.
    #     Same as the second to last test in the "Backup Generator Reliability" testset in the REopt Julia package.
    #     """
        
    #     post_sim = json.load(open(self.post_sim_only, 'rb'))

    #     resp = self.get_response_sim(post_sim)
    #     self.assertHttpCreated(resp)
    #     r_sim = json.loads(resp.content)
    #     #TODO: don't return run_uuid when there's a REoptFailedToStartError
    #     erp_run_uuid = r_sim.get('run_uuid')

    #     resp = self.get_results_sim(erp_run_uuid)
    #     results = json.loads(resp.content)

    #     self.assertAlmostEqual(results["outputs"]["mean_cumulative_survival_final_time_step"], 0.904242, places=4) #0.990784, places=4)
    
    # def test_erp_help_view(self):
    #     """
    #     Tests hiting the erp/help url to get defaults and other info about inputs
    #     """
        
    #     resp = self.get_help()
    #     self.assertHttpOK(resp)
    #     resp = json.loads(resp.content)

    #     resp = self.get_chp_defaults("recip_engine", True, 10000)
    #     self.assertHttpOK(resp)
    #     resp = json.loads(resp.content)
    