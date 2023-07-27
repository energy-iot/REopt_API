
import json
from tastypie.test import ResourceTestCaseMixin
from django.test import TestCase  # have to use unittest.TestCase to get tests to store to database, django.test.TestCase flushes db
import logging
import os
import requests
logging.disable(logging.CRITICAL)

class TestHTTPEndpoints(ResourceTestCaseMixin, TestCase):

    def test_chp_defaults(self):

        inputs = {"hot_water_or_steam": "hot_water",
                "avg_boiler_fuel_load_mmbtu_per_hour": 28.0
        }

        # Direct call of the http.jl endpoint /chp_defaults
        julia_host = os.environ.get('JULIA_HOST', "julia")
        response = requests.get("http://" + julia_host + ":8081/chp_defaults/", json=inputs)
        http_response = response.json()

        # Call to the django view endpoint /chp_defaults which calls the http.jl endpoint
        resp = self.api_client.get(f'/dev/chp_defaults', data=inputs)
        view_response = json.loads(resp.content)

        mismatch = []
        for k, v in http_response["default_inputs"].items():
            if v != view_response["default_inputs"][k]:
                mismatch.append(k)
        
        self.assertEqual(mismatch, [])

        # Check the endpoint logic with the expected selection
        self.assertEqual(http_response["prime_mover"], "combustion_turbine")
        self.assertEqual(http_response["size_class"], 3)
        self.assertGreater(http_response["chp_elec_size_heuristic_kw"], 3500.0)

        # Check that size_class logic is the same
        # Modify input names for v2
        inputs_v2 = {
            "existing_boiler_production_type_steam_or_hw": inputs["hot_water_or_steam"],
            "avg_boiler_fuel_load_mmbtu_per_hr": inputs["avg_boiler_fuel_load_mmbtu_per_hour"]
        }
        resp = self.api_client.get(f'/v2/chp_defaults', data=inputs_v2)
        v2_response = json.loads(resp.content)
        self.assertEqual(http_response["size_class"], v2_response["size_class"])

    def test_absorption_chiller_defaults(self):

        inputs = {"thermal_consumption_hot_water_or_steam": "hot_water",
                "load_max_tons": 50
        }

        # Direct call of the http.jl endpoint /absorption_chiller_defaults
        julia_host = os.environ.get('JULIA_HOST', "julia")
        response = requests.get("http://" + julia_host + ":8081/absorption_chiller_defaults/", json=inputs)
        http_response = response.json()

        # Call to the django view endpoint /absorption_chiller_defaults which calls the http.jl endpoint
        resp = self.api_client.get(f'/dev/absorption_chiller_defaults', data=inputs)
        view_response = json.loads(resp.content)

        mismatch = []
        for k, v in http_response["default_inputs"].items():
            if v != view_response["default_inputs"][k]:
                mismatch.append(k)
        
        self.assertEqual(mismatch, [])

        # Check the endpoint logic with the expected selection
        self.assertEqual(http_response["thermal_consumption_hot_water_or_steam"], "hot_water")
        self.assertEqual(http_response["default_inputs"]["om_cost_per_ton"], 80.0)
        self.assertEqual(http_response["default_inputs"]["installed_cost_per_ton"], 3066.0)
        self.assertEqual(http_response["default_inputs"]["cop_thermal"], 0.74)
        self.assertNotIn("thermal_consumption_hot_water_or_steam", http_response["default_inputs"].keys())
    
    def test_simulated_load(self):

        # Test heating load because REopt.jl separates SpaceHeating and DHW, so had to aggregate for this endpoint
        inputs = {"load_type": "heating",
                "doe_reference_name": "Hospital",
                "latitude": 37.78,
                "longitude": -122.45
        }

        # The /dev/simulated_load endpoint calls the http.jl /simulated_load endpoint
        response = self.api_client.get(f'/dev/simulated_load', data=inputs)
        http_response = json.loads(response.content)

        # Call to the v2 /simulated_load to check for consistency
        resp = self.api_client.get(f'/v2/simulated_load', data=inputs)
        v2_response = json.loads(resp.content)     
        self.assertAlmostEqual(http_response["annual_mmbtu"], v2_response["annual_mmbtu"], delta=1.0)

        # Test blended/hybrid buildings
        inputs["load_type"] = "electric"
        inputs["annual_kwh"] = 1.5E7
        inputs["doe_reference_name[0]"] = "Hospital"
        inputs["doe_reference_name[1]"] = "LargeOffice"
        inputs["percent_share[0]"] = 25.0
        inputs["percent_share[1]"] = 100.0 - inputs["percent_share[0]"]
        
        # The /dev/simulated_load endpoint calls the http.jl /simulated_load endpoint
        response = self.api_client.get(f'/dev/simulated_load', data=inputs)
        http_response = json.loads(response.content)

        # Call to the v2 /simulated_load to check for consistency
        resp = self.api_client.get(f'/v2/simulated_load', data=inputs)
        v2_response = json.loads(resp.content)     
        self.assertAlmostEqual(http_response["annual_kwh"], v2_response["annual_kwh"], delta=1.0)        

        # Test bad inputs
        inputs["invalid_key"] = "invalid_val"
        resp = self.api_client.get(f'/v2/simulated_load', data=inputs)
        v2_response = json.loads(resp.content)   
        assert("Error" in v2_response.keys())

    def test_avert_emissions_profile_endpoint(self):
        # Call to the django view endpoint dev/avert_emissions_profile which calls the http.jl endpoint
        inputs = {
            "latitude": 47.606211,
            "longitude": -122.336052,
            "load_year": 2021
        }
        resp = self.api_client.get(f'/dev/avert_emissions_profile', data=inputs)
        self.assertHttpOK(resp)
        view_response = json.loads(resp.content)
        self.assertEquals(view_response["avert_meters_to_region"], 0.0)
        self.assertEquals(view_response["avert_region"], "Northwest")
        self.assertEquals(len(view_response["emissions_factor_series_lb_NOx_per_kwh"]), 8760)
        inputs = {
            "latitude": 47.606211,
            "longitude": 122.336052,
            "load_year": 2022
        }
        resp = self.api_client.get(f'/dev/avert_emissions_profile', data=inputs)
        self.assertHttpBadRequest(resp)
        view_response = json.loads(resp.content)
        self.assertTrue("error" in view_response)

    def test_cambium_emissions_profile_endpoint(self):
        # Call to the django view endpoint dev/cambium_emissions_profile which calls the http.jl endpoint
        inputs = {
            "load_year": 2021,
            "scenario": "Electricifcation",
            "location_type": "GEA Regions", 
            "latitude": 47.606211, # Seattle 
            "longitude": -122.336052, # Seattle 
            "start_year": 2025,
            "lifetime": 25,
            "metric_col": "lrmer_co2_c",
            "grid_level": "enduse",
            "load_year": 2018
        }
        resp = self.api_client.get(f'/dev/cambium_emissions_profile', data=inputs)
        self.assertHttpOK(resp)
        view_response = json.loads(resp.content)
        self.assertEquals(view_response["metric_col"], "lrmer_co2_c")
        self.assertEquals(view_response["location"], "NWPPc") 
        self.assertEquals(len(view_response["emissions_factor_series_lb_CO2_per_kwh"]), 8760)
        inputs["longitude"] = 122.336052 # China
        resp = self.api_client.get(f'/dev/cambium_emissions_profile', data=inputs)
        self.assertHttpBadRequest(resp) # TODO: check this
        view_response = json.loads(resp.content)
        self.assertTrue("error" in view_response)

    def test_easiur_endpoint(self):
        # Call to the django view endpoint dev/easiur_costs which calls the http.jl endpoint
        inputs = {
            "latitude": 47.606211,
            "longitude": -122.336052,
            "inflation": 0.025
        }
        resp = self.api_client.get(f'/dev/easiur_costs', data=inputs)
        self.assertHttpOK(resp)
        view_response = json.loads(resp.content)
        for ekey in ["NOx", "SO2", "PM25"]:
            for key_format in ["{}_grid_cost_per_tonne", "{}_onsite_fuelburn_cost_per_tonne", "{}_cost_escalation_rate_fraction"]:
                self.assertTrue(type(view_response[key_format.format(ekey)]) == float)
        inputs = {
            "latitude": 47.606211,
            "longitude": 122.336052,
            "inflation": 0.025
        }
        resp = self.api_client.get(f'/dev/easiur_costs', data=inputs)
        self.assertHttpBadRequest(resp)
        view_response = json.loads(resp.content)
        self.assertTrue("error" in view_response)

# For POSTing to an endpoint which returns a `run_uuid` to later GET the results from the database
# resp = self.api_client.post('/dev/job/', format='json', data=scenario))
# self.assertHttpCreated(resp)
# r = json.loads(resp.content)
# run_uuid = r.get('run_uuid')

# This method is used for calling a REopt_API endpoint (/ghpghx) from within the scenario.py celery task
# client = TestApiClient()
# ghpghx_results_url = "/v1/ghpghx/"+ghpghx_uuid_list[i]+"/results/"
# ghpghx_results_resp = client.get(ghpghx_results_url)  # same as doing ghpModelManager.make_response(ghp_uuid)
# ghpghx_results_resp_dict = json.loads(ghpghx_results_resp.content)