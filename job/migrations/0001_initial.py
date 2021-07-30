# Generated by Django 3.1.8 on 2021-07-30 21:17

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_uuid', models.UUIDField(unique=True)),
                ('api_version', models.IntegerField(default=2)),
                ('user_uuid', models.TextField(blank=True, help_text='The assigned unique ID of a signed in REopt user.', null=True)),
                ('webtool_uuid', models.TextField(blank=True, help_text="The unique ID of a scenario created by the REopt Lite Webtool. Note that this ID can be shared by several REopt Lite API Scenarios (for example when users select a 'Resilience' analysis more than one REopt API Scenario is created).", null=True)),
                ('job_type', models.TextField(default='developer.nrel.gov')),
                ('description', models.TextField(blank=True)),
                ('status', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='ElectricLoadInputs',
            fields=[
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='job.scenario')),
                ('annual_kwh', models.FloatField(blank=True, help_text="Annual site energy consumption from electricity, in kWh, used to scale simulated default building load profile for the site's climate zone", null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)])),
                ('doe_reference_name', models.TextField(blank=True, choices=[('FastFoodRest', 'Fastfoodrest'), ('FullServiceRest', 'Fullservicerest'), ('Hospital', 'Hospital'), ('LargeHotel', 'Largehotel'), ('LargeOffice', 'Largeoffice'), ('MediumOffice', 'Mediumoffice'), ('MidriseApartment', 'Midriseapartment'), ('Outpatient', 'Outpatient'), ('PrimarySchool', 'Primaryschool'), ('RetailStore', 'Retailstore'), ('SecondarySchool', 'Secondaryschool'), ('SmallHotel', 'Smallhotel'), ('SmallOffice', 'Smalloffice'), ('StripMall', 'Stripmall'), ('Supermarket', 'Supermarket'), ('Warehouse', 'Warehouse'), ('FlatLoad', 'Flatload'), ('FlatLoad_24_5', 'Flatload 24 5'), ('FlatLoad_16_7', 'Flatload 16 7'), ('FlatLoad_16_5', 'Flatload 16 5'), ('FlatLoad_8_7', 'Flatload 8 7'), ('FlatLoad_8_5', 'Flatload 8 5')], help_text="Simulated load profile from DOE <a href='https: //energy.gov/eere/buildings/commercial-reference-buildings' target='blank'>Commercial Reference Buildings</a>")),
                ('year', models.IntegerField(blank=True, default=2020, help_text="Year of Custom Load Profile. If a custom load profile is uploaded via the loads_kw parameter, it is important that this year correlates with the load profile so that weekdays/weekends are determined correctly for the utility rate tariff. If a DOE Reference Building profile (aka 'simulated' profile) is used, the year is set to 2017 since the DOE profiles start on a Sunday.", null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('monthly_totals_kwh', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)]), blank=True, default=list, help_text="Monthly site energy consumption from electricity series (an array 12 entries long), in kWh, used to scale simulated default building load profile for the site's climate zone", size=None)),
                ('loads_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Typical load over all hours in one year. Must be hourly (8,760 samples), 30 minute (17,520 samples), or 15 minute (35,040 samples). All non-net load values must be greater than or equal to zero. ', size=None)),
                ('critical_loads_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Critical load during an outage period. Must be hourly (8,760 samples), 30 minute (17,520 samples),or 15 minute (35,040 samples). All non-net load values must be greater than or equal to zero.', size=None)),
                ('loads_kw_is_net', models.BooleanField(blank=True, default=True, help_text='If there is existing PV, must specify whether provided load is the net load after existing PV or not.', null=True)),
                ('critical_loads_kw_is_net', models.BooleanField(blank=True, default=False, help_text='If there is existing PV, must specify whether provided load is the net load after existing PV or not.', null=True)),
                ('critical_load_pct', models.FloatField(blank=True, default=0.5, help_text='Critical load factor is multiplied by the typical load to determine the critical load that must be met during an outage. Value must be between zero and one, inclusive.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='ElectricTariffInputs',
            fields=[
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='job.scenario')),
                ('monthly_demand_rates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Array (length of 12) of blended demand charges in dollars per kW', size=12)),
                ('monthly_energy_rates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Array (length of 12) of blended energy rates in dollars per kWh.', size=12)),
                ('urdb_label', models.TextField(blank=True, help_text="Label attribute of utility rate structure from <a href='https://openei.org/services/doc/rest/util_rates/?version=3' target='blank'>Utility Rate Database API</a>")),
                ('urdb_response', picklefield.fields.PickledObjectField(blank=True, editable=False, help_text="Utility rate structure from <a href='https://openei.org/services/doc/rest/util_rates/?version=3' target='blank'>Utility Rate Database API</a>", null=True)),
                ('urdb_rate_name', models.TextField(blank=True, help_text="Name of utility rate from <a href='https://openei.org/wiki/Utility_Rate_Database' target='blank'>Utility Rate Database</a>")),
                ('urdb_utility_name', models.TextField(blank=True, help_text="Name of Utility from <a href='https://openei.org/wiki/Utility_Rate_Database' target='blank'>Utility Rate Database</a>")),
                ('blended_annual_demand_charge', models.FloatField(blank=True, help_text='Annual blended demand rates (annual demand charge cost in $ divided by annual peak demand in kW)', null=True)),
                ('blended_annual_energy_rate', models.FloatField(blank=True, help_text='Annual blended energy rate (total annual energy in kWh divided by annual cost in $)', null=True)),
                ('wholesale_rate', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)]), blank=True, default=list, help_text='Price of electricity sold back to the grid in absence of net metering. Can be a scalar value, which applies for all-time, or an array with time-sensitive values. If an array is input then it must have a length of 8760, 17520, or 35040. The inputed arrayvalues are up/down-sampled using mean values to match the Settings.time_steps_per_hour.', size=None)),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='ElectricTariffOutputs',
            fields=[
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='job.scenario')),
                ('emissions_region', models.TextField(blank=True, null=True)),
                ('year_one_energy_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal year one utility energy cost', null=True)),
                ('year_one_demand_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal year one utility demand cost', null=True)),
                ('year_one_fixed_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal year one utility fixed cost', null=True)),
                ('year_one_min_charge_adder_us_dollars', models.FloatField(blank=True, help_text='Optimal year one utility minimum charge adder', null=True)),
                ('year_one_energy_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one utility energy cost', null=True)),
                ('year_one_demand_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one utility demand cost', null=True)),
                ('year_one_fixed_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one utility fixed cost', null=True)),
                ('year_one_min_charge_adder_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one utility minimum charge adder', null=True)),
                ('total_energy_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal total utility energy cost over the analysis period, after-tax', null=True)),
                ('total_demand_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal total lifecycle utility demand cost over the analysis period, after-tax', null=True)),
                ('total_fixed_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal total utility fixed cost over the analysis period, after-tax', null=True)),
                ('total_min_charge_adder_us_dollars', models.FloatField(blank=True, help_text='Optimal total utility minimum charge adder over the analysis period, after-tax', null=True)),
                ('total_energy_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual total utility energy cost over the analysis period, after-tax', null=True)),
                ('total_demand_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual total lifecycle utility demand cost over the analysis period, after-tax', null=True)),
                ('total_fixed_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual total utility fixed cost over the analysis period, after-tax', null=True)),
                ('total_min_charge_adder_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual total utility minimum charge adder over the analysis period, after-tax', null=True)),
                ('total_export_benefit_us_dollars', models.FloatField(blank=True, help_text='Optimal total value of exported energy over the analysis period, after-tax', null=True)),
                ('total_export_benefit_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual total value of exported energy over the analysis period, after-tax', null=True)),
                ('year_one_bill_us_dollars', models.FloatField(blank=True, help_text='Optimal year one total utility bill', null=True)),
                ('year_one_bill_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one total utility bill', null=True)),
                ('year_one_export_benefit_us_dollars', models.FloatField(blank=True, help_text='Optimal year one value of exported energy', null=True)),
                ('year_one_export_benefit_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one value of exported energy', null=True)),
                ('year_one_energy_cost_series_us_dollars_per_kwh', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Optimal year one hourly energy costs', size=None)),
                ('year_one_demand_cost_series_us_dollars_per_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Optimal year one hourly demand costs', size=None)),
                ('year_one_to_load_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Optimal year one grid to load time series', size=None)),
                ('year_one_to_load_series_bau_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Business as usual year one grid to load time series', size=None)),
                ('year_one_to_battery_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Optimal year one grid to battery time series', size=None)),
                ('year_one_energy_supplied_kwh', models.FloatField(blank=True, help_text='Year one energy supplied from grid to load', null=True)),
                ('year_one_energy_supplied_kwh_bau', models.FloatField(blank=True, help_text='Year one energy supplied from grid to load', null=True)),
                ('year_one_emissions_lb_C02', models.FloatField(blank=True, help_text='Optimal year one equivalent pounds of carbon dioxide emitted from utility electricity use. Calculated from EPA AVERT region hourly grid emissions factor series for the continental US.In AK and HI, the best available data are EPA eGRID annual averages.', null=True)),
                ('year_one_emissions_bau_lb_C02', models.FloatField(blank=True, help_text='Business as usual year one equivalent pounds of carbon dioxide emitted from utility electricity use. Calculated from EPA AVERT region hourly grid emissions factor series for the continental US.In AK and HI, the best available data are EPA eGRID annual averages.', null=True)),
                ('year_one_coincident_peak_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal year one coincident peak charges', null=True)),
                ('year_one_coincident_peak_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual year one coincident peak charges', null=True)),
                ('total_coincident_peak_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal total coincident peak charges over the analysis period, after-tax', null=True)),
                ('total_coincident_peak_cost_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual total coincident peak charges over the analysis period, after-tax', null=True)),
                ('year_one_chp_standby_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal year one standby charge cost incurred by CHP', null=True)),
                ('total_chp_standby_cost_us_dollars', models.FloatField(blank=True, help_text='Optimal total standby charge cost incurred by CHP over the analysis period, after-tax', null=True)),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='ElectricUtilityInputs',
            fields=[
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='job.scenario')),
                ('outage_start_time_step', models.IntegerField(blank=True, help_text='Time step that grid outage starts. Must be less than outage_end.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(35040)])),
                ('outage_end_time_step', models.IntegerField(blank=True, help_text='Time step that grid outage ends. Must be greater than outage_start.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(35040)])),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='job.scenario')),
                ('timeout_seconds', models.IntegerField(default=420, help_text='The number of seconds allowed before the optimization times out.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(420)])),
                ('time_steps_per_hour', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (4, 'Four')], default=1, help_text='The number of time steps per hour in the REopt model.')),
                ('optimality_tolerance', models.FloatField(default=0.001, help_text="The threshold for the difference between the solution's objective value and the best possible value at which the solver terminates", validators=[django.core.validators.MinValueValidator(1e-05), django.core.validators.MaxValueValidator(10)])),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='SiteInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='The approximate latitude of the site in decimal degrees.', validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(help_text='The approximate longitude of the site in decimal degrees.', validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('land_acres', models.FloatField(blank=True, help_text='Land area in acres available for PV panel siting', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)])),
                ('roof_squarefeet', models.FloatField(blank=True, help_text='Area of roof in square feet available for PV siting', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SiteInputs', to='job.scenario')),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='PVInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pv_number', models.IntegerField(blank=True, help_text='Index out of all PV system models', null=True)),
                ('pv_name', models.TextField(blank=True, help_text='PV name/description')),
                ('existing_kw', models.FloatField(blank=True, default=0, help_text='Existing PV size', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000.0)])),
                ('min_kw', models.FloatField(blank=True, default=0, help_text='Minimum PV size constraint for optimization', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('max_kw', models.FloatField(blank=True, default=1000000000.0, help_text='Maximum PV size constraint for optimization. Set to zero to disable PV', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('installed_cost_us_dollars_per_kw', models.FloatField(blank=True, default=1600, help_text='Installed PV cost in $/kW', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000.0)])),
                ('om_cost_us_dollars_per_kw', models.FloatField(blank=True, default=16, help_text='Annual PV operations and maintenance costs in $/kW', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000.0)])),
                ('macrs_option_years', models.IntegerField(blank=True, choices=[(0, 'Zero'), (5, 'Five'), (7, 'Seven')], default=5, help_text='Duration over which accelerated depreciation will occur. Set to zero to disable', null=True)),
                ('macrs_bonus_pct', models.FloatField(blank=True, default=0, help_text='Percent of upfront project costs to depreciate in year one in addition to scheduled depreciation', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('macrs_itc_reduction', models.FloatField(blank=True, default=0.5, help_text='Percent of the ITC value by which depreciable basis is reduced', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('federal_itc_pct', models.FloatField(blank=True, default=0.26, help_text='Percentage of capital costs that are credited towards federal taxes', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('state_ibi_pct', models.FloatField(blank=True, default=0, help_text='Percentage of capital costs offset by state incentives', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('state_ibi_max_us_dollars', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum dollar value of state percentage-based capital cost incentive', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('utility_ibi_pct', models.FloatField(blank=True, default=0, help_text='Percentage of capital costs offset by utility incentives', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('utility_ibi_max_us_dollars', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum dollar value of utility percentage-based capital cost incentive', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('federal_rebate_us_dollars_per_kw', models.FloatField(blank=True, default=0, help_text='Federal rebates based on installed capacity', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('state_rebate_us_dollars_per_kw', models.FloatField(blank=True, default=0, help_text='State rebate based on installed capacity', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('state_rebate_max_us_dollars', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum state rebate', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('utility_rebate_us_dollars_per_kw', models.FloatField(blank=True, default=0, help_text='Utility rebate based on installed capacity', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('utility_rebate_max_us_dollars', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum utility rebate', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('pbi_us_dollars_per_kwh', models.FloatField(blank=True, default=0, help_text='Production-based incentive value', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('pbi_max_us_dollars', models.FloatField(blank=True, default=1000000000.0, help_text='Maximum annual value in present terms of production-based incentives', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('pbi_years', models.FloatField(blank=True, default=1, help_text='Duration of production-based incentives from installation date', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('pbi_system_max_kw', models.FloatField(blank=True, default=1000000000.0, help_text='Maximum system size eligible for production-based incentive', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('degradation_pct', models.FloatField(blank=True, default=0.005, help_text='Annual rate of degradation in PV energy production', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('azimuth', models.FloatField(blank=True, default=180, help_text='PV azimuth angle', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('losses', models.FloatField(blank=True, default=0.14, help_text='PV system performance losses', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0.99)])),
                ('array_type', models.IntegerField(blank=True, choices=[(0, 'Ground Mount Fixed Open Rack'), (1, 'Rooftop Fixed'), (2, 'Ground Mount One Axis Tracking'), (3, 'One Axis Backtracking'), (4, 'Ground Mount Two Axis Tracking')], default=1, help_text='PV Watts array type (0: Ground Mount Fixed (Open Rack); 1: Rooftop, Fixed; 2: Ground Mount 1-Axis Tracking; 3 : 1-Axis Backtracking; 4: Ground Mount, 2-Axis Tracking)', null=True)),
                ('module_type', models.IntegerField(blank=True, choices=[(0, 'Standard'), (1, 'Premium'), (2, 'Thin Film')], default=0, help_text='PV module type (0: Standard; 1: Premium; 2: Thin Film)', null=True)),
                ('gcr', models.FloatField(blank=True, default=0.4, help_text='PV ground cover ratio (photovoltaic array area : total ground area).', null=True, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(0.99)])),
                ('dc_ac_ratio', models.FloatField(blank=True, default=0.023, help_text='PV DC-AC ratio', null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)])),
                ('inv_eff', models.FloatField(blank=True, default=0.96, help_text='PV inverter efficiency', null=True, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(0.995)])),
                ('radius', models.FloatField(blank=True, default=0, help_text='Radius, in miles, to use when searching for the closest climate data station. Use zero to use the closest station regardless of the distance', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('tilt', models.FloatField(blank=True, default=0.537, help_text='PV system tilt', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)])),
                ('location', models.TextField(blank=True, choices=[('roof', 'Roof'), ('ground', 'Ground'), ('both', 'Both')], default='both', help_text='Where PV can be deployed. One of [roof, ground, both] with default as both')),
                ('prod_factor_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Optional user-defined production factors. Entries have units of kWh/kW, representing the energy (kWh) output of a 1 kW system in each time step. Must be hourly (8,760 samples), 30 minute (17,520 samples), or 15 minute (35,040 samples).', size=None)),
                ('can_net_meter', models.BooleanField(blank=True, default=True, help_text='True/False for if technology has option to participate in net metering agreement with utility. Note that a technology can only participate in either net metering or wholesale rates (not both).', null=True)),
                ('can_wholesale', models.BooleanField(blank=True, default=True, help_text='True/False for if technology has option to export energy that is compensated at the wholesale_rate. Note that a technology can only participate in either net metering or wholesale rates (not both).', null=True)),
                ('can_export_beyond_site_load', models.BooleanField(blank=True, default=True, help_text='True/False for if technology can export energy beyond the annual site load (and be compensated for that energy at the wholesale_rate_above_site_load_us_dollars_per_kwh).', null=True)),
                ('can_curtail', models.BooleanField(blank=True, default=True, help_text='True/False for if technology can curtail energy produced.', null=True)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.scenario')),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.TextField(default='')),
                ('message', models.TextField(default='')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialOutputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lcc_us_dollars', models.FloatField(blank=True, help_text='Optimal lifecycle cost', null=True)),
                ('lcc_bau_us_dollars', models.FloatField(blank=True, help_text='Business as usual lifecycle cost', null=True)),
                ('npv_us_dollars', models.FloatField(blank=True, help_text='Net present value of savings realized by the project', null=True)),
                ('net_capital_costs_plus_om_us_dollars', models.FloatField(blank=True, help_text='Capital cost for all technologies plus present value of operations and maintenance over anlaysis period', null=True)),
                ('net_om_us_dollars_bau', models.FloatField(blank=True, help_text='Business-as-usual present value of operations and maintenance over anlaysis period', null=True)),
                ('net_capital_costs', models.FloatField(blank=True, help_text='Net capital costs for all technologies, in present value, including replacement costs and incentives.', null=True)),
                ('microgrid_upgrade_cost', models.FloatField(blank=True, help_text='Cost to make a distributed energy system islandable from the grid. Determined by multiplying the total capital costs of resultant energy systems from REopt (such as PV and Storage system) with the input value for microgrid_upgrade_cost_pct (which defaults to 0.30).', null=True)),
                ('initial_capital_costs', models.FloatField(blank=True, help_text='Up-front capital costs for all technologies, in present value, excluding replacement costs and incentives.', null=True)),
                ('initial_capital_costs_after_incentives', models.FloatField(blank=True, help_text='Up-front capital costs for all technologies, in present value, excluding replacement costs, including incentives.', null=True)),
                ('replacement_costs', models.FloatField(blank=True, help_text='Net replacement costs for all technologies, in future value, excluding incentives.', null=True)),
                ('om_and_replacement_present_cost_after_tax_us_dollars', models.FloatField(blank=True, help_text='Net O&M and replacement costs in present value, after-tax.', null=True)),
                ('total_om_costs_us_dollars', models.FloatField(blank=True, help_text='Total operations and maintenance cost over analysis period.', null=True)),
                ('year_one_om_costs_us_dollars', models.FloatField(blank=True, help_text='Year one operations and maintenance cost after tax.', null=True)),
                ('year_one_om_costs_before_tax_us_dollars', models.FloatField(blank=True, help_text='Year one operations and maintenance cost before tax.', null=True)),
                ('simple_payback_years', models.FloatField(blank=True, help_text='Number of years until the cumulative annual cashflow turns positive. If the cashflow becomes negative again after becoming positive (i.e. due to battery repalcement costs) then simple payback is increased by the number of years that the cash flow is negative beyond the break-even year.', null=True)),
                ('irr_pct', models.FloatField(blank=True, help_text='internal Rate of Return of the cost-optimal system. In two-party cases the developer discount rate is used in place of the offtaker discount rate.', null=True)),
                ('net_present_cost_us_dollars', models.FloatField(blank=True, help_text='Present value of the total costs incurred by the third-party owning and operating the distributed energy resource assets.', null=True)),
                ('annualized_payment_to_third_party_us_dollars', models.FloatField(blank=True, help_text='The annualized amount the host will pay to the third-party owner over the life of the project.', null=True)),
                ('offtaker_annual_free_cashflow_series', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Annual free cashflow for the host in the optimal case for all analysis years, including year 0. Future years have not been discounted to account for the time value of money.', size=None)),
                ('offtaker_discounted_annual_free_cashflow_series_us_dollars', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Annual discounted free cashflow for the host in the optimal case for all analysis years, including year 0. Future years have been discounted to account for the time value of money.', size=None)),
                ('offtaker_annual_free_cashflow_series_bau_us_dollars', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Annual free cashflow for the host in the business-as-usual case for all analysis years, including year 0. Future years have not been discounted to account for the time value of money. Only calculated in the non-third-party case.', size=None)),
                ('offtaker_discounted_annual_free_cashflow_series_bau_us_dollars', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Annual discounted free cashflow for the host in the business-as-usual case for all analysis years, including year 0. Future years have been discounted to account for the time value of money. Only calculated in the non-third-party case.', null=True, size=None)),
                ('developer_annual_free_cashflow_series_us_dollars', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Annual free cashflow for the developer in the business-as-usual third party case for all analysis years, including year 0. Future years have not been discounted to account for the time value of money. Only calculated in the third-party case.', size=None)),
                ('developer_om_and_replacement_present_cost_after_tax_us_dollars', models.FloatField(blank=True, help_text='Net O&M and replacement costs in present value, after-tax for the third-party developer. Only calculated in the third-party case.', null=True)),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='FinancialOutputs', to='job.scenario')),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='FinancialInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_years', models.IntegerField(blank=True, default=25, help_text='Analysis period in years. Must be integer.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(75)])),
                ('elec_cost_escalation_pct', models.FloatField(blank=True, default=0.023, help_text='Annual nominal utility electricity cost escalation rate.', null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)])),
                ('offtaker_discount_pct', models.FloatField(blank=True, default=0.083, help_text='Nominal energy offtaker discount rate. In single ownership model the offtaker is also the generation owner.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('offtaker_tax_pct', models.FloatField(blank=True, default=0.26, help_text='Host tax rate', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0.999)])),
                ('om_cost_escalation_pct', models.FloatField(blank=True, default=0.025, help_text='Annual nominal O&M cost escalation rate', null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)])),
                ('owner_discount_pct', models.FloatField(blank=True, default=0.083, help_text='Nominal generation owner discount rate. Used for two party financing model. In two party ownership model the offtaker does not own the generator(s).', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('owner_tax_pct', models.FloatField(blank=True, default=0.26, help_text='Generation owner tax rate. Used for two party financing model. In two party ownership model the offtaker does not own the generator(s).', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0.999)])),
                ('third_party_ownership', models.BooleanField(blank=True, default=False, help_text='Specify if ownership model is direct ownership or two party. In two party model the offtaker does not purcharse the generation technologies, but pays the generation owner for energy from the generator(s).', null=True)),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='FinancialInputs', to='job.scenario')),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
    ]
