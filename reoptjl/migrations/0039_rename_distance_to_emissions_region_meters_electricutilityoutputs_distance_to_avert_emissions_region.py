# Generated by Django 4.0.7 on 2023-07-27 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0038_alter_generatorinputs_installed_cost_per_kw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricutilityoutputs',
            old_name='distance_to_emissions_region_meters',
            new_name='distance_to_avert_emissions_region_meters',
        ),
        migrations.RemoveField(
            model_name='electricutilityinputs',
            name='emissions_region',
        ),
        migrations.RemoveField(
            model_name='electricutilityoutputs',
            name='emissions_region',
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='allow_simultaneous_export_import',
            field=models.BooleanField(blank=True, default=True, help_text='If true the site has two meters (in effect).'),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='avert_emissions_region',
            field=models.TextField(blank=True, help_text="Name of the AVERT emissions region to use. Options are: 'California', 'Central', 'Florida', 'Mid-Atlantic', 'Midwest', 'Carolinas', 'New England', 'Northwest', 'New York', 'Rocky Mountains', 'Southeast', 'Southwest', 'Tennessee', 'Texas', 'Alaska', 'Hawaii (except Oahu)', 'Hawaii (Oahu)'. If emissions_factor_series_lb_<pollutant>_per_kwh inputs are not provided, avert_emissions_region overrides latitude and longitude in determining emissions factors."),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='cambium_grid_level',
            field=models.TextField(blank=True, default='enduse', help_text='Impacts grid climate emissions calculation. Options: enduse or busbar. Busbar refers to point where bulk generating stations connect to grid; enduse refers to point of consumption (includes distribution loss rate).'),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='cambium_levelization_years',
            field=models.IntegerField(blank=True, help_text='Expected lifetime or analysis period of the intervention being studied. Emissions will be averaged over this period. Default: analysis_years (from Financial struct)', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='cambium_location_type',
            field=models.TextField(blank=True, default='States', help_text="Geographic boundary at which emissions are calculated. Options: ['Nations', 'GEA Regions', 'States', 'Balancing Areas']."),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='cambium_metric_col',
            field=models.TextField(blank=True, default='lrmer_co2e', help_text='Emissions metric used. Default is Long-run marginal emissions rate for CO2-equivalant, combined combustion and pre-combustion emissions rates. Options: See metric definitions and names in the Cambium documentation.'),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='cambium_scenario',
            field=models.TextField(blank=True, default='Mid-case', help_text="Cambium Scenario for evolution of electricity sector (see Cambium documentation for descriptions).Options: ['Mid-case', 'Low Renewable Energy and Battery Costs', 'High Renewable Energy and Battery Costs', 'Electricifcation', 'Low Natural Gas Price', 'High Natural Gas Price', 'Mid-case with 95% Decarbonization by 2050', 'Mid-case with 100% Decarbonization by 2035', 'Mid-case (with tax credit phaseout)', 'Low Renewable Energy and Battery Costs (with tax credit phaseout)']"),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='cambium_start_year',
            field=models.IntegerField(blank=True, default=2024, help_text='First year of operation of system. Emissions will be levelized starting in this year for the duration of cambium_levelization_years.', validators=[django.core.validators.MinValueValidator(2023), django.core.validators.MaxValueValidator(2050)]),
        ),
        migrations.AddField(
            model_name='electricutilityinputs',
            name='co2_from_avert',
            field=models.BooleanField(blank=True, default=False, help_text="Default is to use Cambium data for CO2 grid emissions. Set to `true` to instead use data from the EPA's AVERT database. "),
        ),
        migrations.AddField(
            model_name='electricutilityoutputs',
            name='avert_emissions_region',
            field=models.TextField(blank=True, help_text="Name of the AVERT emissions region. Determined from site longitude and latitude if avert_emissions_region and emissions_factor_series_lb_<pollutant>_per_kwh inputs were not provided. Used to populate health emissions factors by default and climate emissions factors if co2_from_avert is set to true.Can be one of: [California', 'Central', 'Florida', 'Mid-Atlantic', 'Midwest', 'Carolinas', 'New England',  'Northwest', 'New York', 'Rocky Mountains', 'Southeast', 'Southwest', 'Tennessee', 'Texas','Alaska', 'Hawaii (except Oahu)', 'Hawaii (Oahu)'] "),
        ),
        migrations.AddField(
            model_name='electricutilityoutputs',
            name='cambium_emissions_region',
            field=models.TextField(blank=True, help_text='Name of the Cambium emissions region used for climate emissions for grid electricity. Determined from site longitude and latitude and the cambium_location_type if custom emissions_factor_series_lb_CO2_per_kwh not provided and co2_from_avert is false.'),
        ),
        migrations.AlterField(
            model_name='electricloadinputs',
            name='critical_load_fraction',
            field=models.FloatField(blank=True, default=0.5, help_text='Critical load factor is multiplied by the typical load to determine the critical load that must be met during an outage. Value must be between zero and one, inclusive.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='electricloadinputs',
            name='critical_loads_kw_is_net',
            field=models.BooleanField(blank=True, default=False, help_text='If there is existing PV, must specify whether provided load is the net load after existing PV or not.'),
        ),
        migrations.AlterField(
            model_name='electricloadinputs',
            name='loads_kw_is_net',
            field=models.BooleanField(blank=True, default=True, help_text='If there is existing PV, must specify whether provided load is the net load after existing PV or not.'),
        ),
        migrations.AlterField(
            model_name='siteinputs',
            name='min_resil_time_steps',
            field=models.IntegerField(blank=True, help_text='The minimum number consecutive timesteps that load must be fully met once an outage begins. Only applies to multiple outage modeling using inputs outage_start_time_steps and outage_durations.If no value is provided, will default to max([ElectricUtility].outage_durations).', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
