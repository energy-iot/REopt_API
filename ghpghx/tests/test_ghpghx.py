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
import copy
from tastypie.test import ResourceTestCaseMixin
from django.test import TestCase
import pandas as pd
from ghpghx.models import ModelManager

class TestGHPGHX(ResourceTestCaseMixin, TestCase): 
    """
    Test GHPGHX model
    """
   
    def setUp(self):
        # setUp() is a standard method which is run for every test (in addition to __init__())
        super(TestGHPGHX, self).setUp()
        self.loads_view = '/v1/simulated_load/'
        self.ghpghx_base = '/v1/ghpghx/'
        self.test_ghpghx_post = os.path.join('ghpghx', 'tests', 'posts', 'test_ghpghx_POST.json')

    def get_loads_response(self, params_dict):
        return self.api_client.get(self.loads_view, data=params_dict)

    def get_ghpghx_response(self, data):
        return self.api_client.post(self.ghpghx_base, format='json', data=data)

    def test_ghpghx(self):

        # Call to GHPGHX app to run GHPGHX model and return the "ghpghx_response" as input to REopt
        ghpghx_post = json.load(open(self.test_ghpghx_post, 'rb'))
        # Get load data from /simulated_load endpoint using the self.test_reopt_post location and building type
        # Lat/long assumed to be generated by the webtool based on "city, state" location
        latitude =  37.78 # 33.7676338
        longitude = -122.45 # -84.5606888
        ghpghx_post["latitude"] = latitude
        ghpghx_post["longitude"] = longitude
        doe_reference_name = "Hospital"
        heating_params = {"latitude": latitude,
                            "longitude": longitude,
                            "doe_reference_name": doe_reference_name,
                            "load_type": "heating"}
        cooling_params = copy.deepcopy(heating_params)
        cooling_params["load_type"] = "electric" # actually cooling is what we want, but with no annual_tonhour we need to ping load_type=electric
        cooling_params["cooling_doe_ref_name"] = doe_reference_name

        heating_load_resp = self.get_loads_response(params_dict=heating_params)  # This is FUEL-based
        heating_load_dict = json.loads(heating_load_resp.content)
        # Only need boiler_efficiency if the user inputs this, otherwise uses default 0.8
        ghpghx_post["existing_boiler_efficiency"] = 1.0
        ghpghx_post["heating_fuel_load_mmbtu_per_hr"] = heating_load_dict["loads_mmbtu"]
        cooling_load_resp = self.get_loads_response(params_dict=cooling_params)
        cooling_load_dict = json.loads(cooling_load_resp.content)
        ghpghx_post["cooling_thermal_load_ton"] = cooling_load_dict["cooling_defaults"]["loads_ton"]

        # Heat pump performance maps
        hp_cop_filepath = os.path.join('ghpghx', 'tests', 'posts', "heatpump_cop_map.csv" )
        heatpump_copmap_df = pd.read_csv(hp_cop_filepath)
        heatpump_copmap_list_of_dict = heatpump_copmap_df.to_dict('records')
        ghpghx_post["cop_map_eft_heating_cooling"] = heatpump_copmap_list_of_dict        


        resp = self.get_ghpghx_response(data=ghpghx_post)
        self.assertHttpCreated(resp)
        r = json.loads(resp.content)

        # Now we should have ghp_uuid from the POST response, and we now need to simulate the /results endpoint to get the data
        # We could instead GET the /results endpoint response using this ghp_uuid, but we have make_response internally
        ghp_uuid = r.get('ghp_uuid')
        results_url = "/v1/ghpghx/"+ghp_uuid+"/results/"
        resp = self.api_client.get(results_url)
        d = json.loads(resp.content)
        
        #d = ModelManager.make_response(ghp_uuid=ghp_uuid)
        #json.dump(d["inputs"], open("ghpghx_post.json", "w"))
        dummy = 3