# Generated by Django 4.0.6 on 2022-10-12 01:56

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_rename_prod_factor_series_pvinputs_production_factor_series_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CHPOutputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_kw', models.FloatField(blank=True, help_text='Power capacity size of the CHP system [kW]', null=True)),
                ('size_supplemental_firing_kw', models.FloatField(blank=True, help_text='Power capacity of CHP supplementary firing system [kW]', null=True)),
                ('year_one_fuel_used_mmbtu', models.FloatField(blank=True, help_text='Fuel consumed in year one [MMBtu]', null=True)),
                ('year_one_electric_energy_produced_kwh', models.FloatField(blank=True, help_text='Electric energy produced in year one [kWh]', null=True)),
                ('year_one_thermal_energy_produced_mmbtu', models.FloatField(blank=True, help_text='Thermal energy produced in year one [MMBtu]', null=True)),
                ('year_one_electric_production_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Electric power production time-series array [kW]', size=None)),
                ('year_one_to_grid_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Electric power exported time-series array [kW]', size=None)),
                ('year_one_to_battery_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Electric power to charge the battery storage time-series array [kW]', size=None)),
                ('year_one_to_load_series_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Electric power to serve the electric load time-series array [kW]', size=None)),
                ('year_one_thermal_to_tes_series_mmbtu_per_hour', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Thermal power to TES time-series array [MMBtu/hr]', size=None)),
                ('year_one_thermal_to_waste_series_mmbtu_per_hour', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Thermal power wasted/unused/vented time-series array [MMBtu/hr]', size=None)),
                ('year_one_thermal_to_load_series_mmbtu_per_hour', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Thermal power to serve the heating load time-series array [MMBtu/hr]', size=None)),
                ('year_one_chp_fuel_cost_before_tax', models.FloatField(blank=True, help_text='Cost of fuel consumed by the CHP system in year one [\\$]', null=True)),
                ('lifecycle_chp_fuel_cost_after_tax', models.FloatField(blank=True, help_text='Present value of cost of fuel consumed by the CHP system, after tax [\\$]', null=True)),
                ('year_one_chp_standby_cost_before_tax', models.FloatField(blank=True, help_text='CHP standby charges in year one [\\$]', null=True)),
                ('lifecycle_chp_standby_cost_after_tax', models.FloatField(blank=True, help_text='Present value of all CHP standby charges, after tax.', null=True)),
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CHPOutputs', to='job.apimeta')),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='CHPInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_cost_per_mmbtu', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)]), blank=True, default=list, help_text='The CHP system fuel cost is a required input when the CHP system is included as an option.The `fuel_cost_per_mmbtu` can be a scalar, a list of 12 monthly values, or a time series of values for every time step.If a scalar or a vector of 12 values are provided, then the value is scaled up to 8760 values.If a vector of 8760, 17520, or 35040 values is provided, it is adjusted to match timesteps per hour in the optimization.', size=None)),
                ('prime_mover', models.TextField(blank=True, choices=[('recip_engine', 'Recip Engine'), ('micro_turbine', 'Micro Turbine'), ('combustion_turbine', 'Combustion Turbine'), ('fuel_cell', 'Fuel Cell')], help_text='CHP prime mover, one of recip_engine, micro_turbine, combustion_turbine, fuel_cell')),
                ('installed_cost_per_kw', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Installed cost in $/kW', null=True, size=None)),
                ('tech_sizes_for_cost_curve', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, help_text='Capacity intervals correpsonding to cost rates in installed_cost_per_kW, in kW', null=True, size=None)),
                ('om_cost_per_kwh', models.FloatField(blank=True, help_text='CHP per unit production (variable) operations and maintenance costs in $/kWh', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('electric_efficiency_half_load', models.FloatField(blank=True, help_text='Electric efficiency of CHP prime-mover at half-load, HHV-basis', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('electric_efficiency_full_load', models.FloatField(blank=True, help_text='Electric efficiency of CHP prime-mover at full-load, HHV-basis', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('min_turn_down_fraction', models.FloatField(blank=True, help_text='Minimum CHP loading in fraction of capacity (size_kw).', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('thermal_efficiency_full_load', models.FloatField(blank=True, help_text='CHP fraction of fuel energy converted to hot-thermal energy at full electric load', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('thermal_efficiency_half_load', models.FloatField(blank=True, help_text='CHP fraction of fuel energy converted to hot-thermal energy at half electric load', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('min_allowable_kw', models.FloatField(blank=True, help_text='Minimum nonzero CHP size (in kWe) (i.e. it is possible to select no CHP system)', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('max_kw', models.FloatField(blank=True, help_text='Maximum CHP size (in kWe) constraint for optimization. Set to zero to disable CHP', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)])),
                ('cooling_thermal_factor', models.FloatField(blank=True, help_text='Knockdown factor on absorption chiller COP based on the CHP prime_mover not being able to produce as high of temp/pressure hot water/steam', null=True, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(1.0)])),
                ('unavailability_periods', django.contrib.postgres.fields.ArrayField(base_field=picklefield.fields.PickledObjectField(editable=False, null=True), blank=True, help_text="CHP unavailability periods for scheduled and unscheduled maintenance, list of dictionaries with keys of ['month', 'start_week_of_month', 'start_day_of_week', 'start_hour', 'duration_hours'] all values are one-indexed and start_day_of_week uses 1 for Monday, 7 for Sunday", null=True, size=None)),
                ('size_class', models.IntegerField(blank=True, default=1, help_text='CHP size class. Must be a strictly positive integer value', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('min_kw', models.FloatField(blank=True, default=0, help_text='Minimum CHP size constraint for optimization', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('fuel_type', models.TextField(blank=True, choices=[('natural_gas', 'Natural Gas'), ('landfill_bio_gas', 'Landfill Bio Gas'), ('propane', 'Propane'), ('diesel_oil', 'Diesel Oil')], default='natural_gas', help_text='Existing CHP fuel type, one of natural_gas, landfill_bio_gas, propane, diesel_oil')),
                ('om_cost_per_kw', models.FloatField(blank=True, help_text='Annual CHP fixed operations and maintenance costs in $/kW', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('om_cost_per_hr_per_kw_rated', models.FloatField(blank=True, default=0.0, help_text='CHP system per-operating-hour (variable) operations and maintenance costs in $/hr-kW', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('supplementary_firing_capital_cost_per_kw', models.FloatField(blank=True, default=150, help_text='Installed CHP supplementary firing system cost in $/kWe', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000.0)])),
                ('supplementary_firing_max_steam_ratio', models.FloatField(blank=True, default=1.0, help_text='Ratio of max fired steam to un-fired steam production. Relevant only for combustion_turbine prime_mover', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('supplementary_firing_efficiency', models.FloatField(blank=True, default=0.92, help_text='Thermal efficiency of the incremental steam production from supplementary firing. Relevant only for combustion_turbine prime_mover', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('standby_rate_per_kw_per_month', models.FloatField(blank=True, default=0, help_text='Standby rate charged to CHP based on CHP electric power size', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('reduces_demand_charges', models.BooleanField(blank=True, default=True, help_text='Boolean indicator if CHP reduces demand charges', null=True)),
                ('can_supply_steam_turbine', models.BooleanField(blank=True, default=False, help_text='Boolean indicator if CHP can supply steam to the steam turbine for electric production', null=True)),
                ('macrs_option_years', models.IntegerField(blank=True, choices=[(0, 'Zero'), (5, 'Five'), (7, 'Seven')], default=0, help_text='Duration over which accelerated depreciation will occur. Set to zero to disable')),
                ('macrs_bonus_fraction', models.FloatField(blank=True, default=1.0, help_text='Percent of upfront project costs to depreciate in year one in addition to scheduled depreciation', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('macrs_itc_reduction', models.FloatField(blank=True, default=0.5, help_text='Percent of the ITC value by which depreciable basis is reduced', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('federal_itc_fraction', models.FloatField(blank=True, default=0.1, help_text='Percentage of capital costs that are credited towards federal taxes', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('federal_rebate_per_kw', models.FloatField(blank=True, default=0, help_text='Federal rebates based on installed capacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('state_ibi_fraction', models.FloatField(blank=True, default=0, help_text='Percentage of capital costs offset by state incentives', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('state_ibi_max', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum dollar value of state percentage-based capital cost incentive', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('state_rebate_per_kw', models.FloatField(blank=True, default=0, help_text='State rebate based on installed capacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('state_rebate_max', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum state rebate', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('utility_ibi_fraction', models.FloatField(blank=True, default=0, help_text='Percentage of capital costs offset by utility incentives', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('utility_ibi_max', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum dollar value of utility percentage-based capital cost incentive', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('utility_rebate_per_kw', models.FloatField(blank=True, default=0, help_text='Utility rebate based on installed capacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('utility_rebate_max', models.FloatField(blank=True, default=10000000000.0, help_text='Maximum utility rebate', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000000.0)])),
                ('production_incentive_per_kwh', models.FloatField(blank=True, default=0, help_text='Production-based incentive value', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('production_incentive_max_benefit', models.FloatField(blank=True, default=1000000000.0, help_text='Maximum annual value in present terms of production-based incentives', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('production_incentive_years', models.IntegerField(blank=True, default=0, help_text='Duration of production-based incentives from installation date', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('production_incentive_max_kw', models.FloatField(blank=True, default=0.0, help_text='Maximum system size eligible for production-based incentive', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('can_net_meter', models.BooleanField(blank=True, default=False, help_text='True/False for if technology has option to participate in net metering agreement with utility. Note that a technology can only participate in either net metering or wholesale rates (not both).')),
                ('can_wholesale', models.BooleanField(blank=True, default=False, help_text='True/False for if technology has option to export energy that is compensated at the wholesale_rate. Note that a technology can only participate in either net metering or wholesale rates (not both).')),
                ('can_export_beyond_nem_limit', models.BooleanField(blank=True, default=False, help_text='True/False for if technology can export energy beyond the annual site load (and be compensated for that energy at the export_rate_beyond_net_metering_limit).')),
                ('can_curtail', models.BooleanField(blank=True, default=False, help_text='True/False for if technology has the ability to curtail energy production.')),
                ('fuel_renewable_energy_fraction', models.FloatField(blank=True, default=0.0, help_text='Fraction of the CHP fuel considered renewable.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('emissions_factor_lb_CO2_per_mmbtu', models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)])),
                ('emissions_factor_lb_NOx_per_mmbtu', models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)])),
                ('emissions_factor_lb_SO2_per_mmbtu', models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)])),
                ('emissions_factor_lb_PM25_per_mmbtu', models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)])),
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CHPInputs', to='job.apimeta')),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
    ]
