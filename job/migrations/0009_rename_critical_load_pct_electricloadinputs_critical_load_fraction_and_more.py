# Generated by Django 4.0.6 on 2022-09-13 21:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_domestichotwaterloadinputs_existingboilerinputs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricloadinputs',
            old_name='critical_load_pct',
            new_name='critical_load_fraction',
        ),
        migrations.RenameField(
            model_name='electricloadinputs',
            old_name='min_load_met_annual_pct',
            new_name='min_load_met_annual_fraction',
        ),
        migrations.RenameField(
            model_name='electricloadinputs',
            old_name='operating_reserve_required_pct',
            new_name='operating_reserve_required_fraction',
        ),
        migrations.RenameField(
            model_name='electricloadoutputs',
            old_name='offgrid_load_met_pct',
            new_name='offgrid_load_met_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='internal_efficiency_pct',
            new_name='internal_efficiency_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='inverter_efficiency_pct',
            new_name='inverter_efficiency_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='macrs_bonus_pct',
            new_name='macrs_bonus_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='rectifier_efficiency_pct',
            new_name='rectifier_efficiency_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='soc_init_pct',
            new_name='soc_init_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='soc_min_pct',
            new_name='soc_min_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageinputs',
            old_name='total_itc_pct',
            new_name='total_itc_fraction',
        ),
        migrations.RenameField(
            model_name='electricstorageoutputs',
            old_name='year_one_soc_series_pct',
            new_name='year_one_soc_series_fraction',
        ),
        migrations.RenameField(
            model_name='electricutilityinputs',
            old_name='emissions_factor_CO2_decrease_pct',
            new_name='emissions_factor_CO2_decrease_fraction',
        ),
        migrations.RenameField(
            model_name='electricutilityinputs',
            old_name='emissions_factor_NOx_decrease_pct',
            new_name='emissions_factor_NOx_decrease_fraction',
        ),
        migrations.RenameField(
            model_name='electricutilityinputs',
            old_name='emissions_factor_PM25_decrease_pct',
            new_name='emissions_factor_PM25_decrease_fraction',
        ),
        migrations.RenameField(
            model_name='electricutilityinputs',
            old_name='emissions_factor_SO2_decrease_pct',
            new_name='emissions_factor_SO2_decrease_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='CO2_cost_escalation_pct',
            new_name='CO2_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='NOx_cost_escalation_pct',
            new_name='NOx_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='PM25_cost_escalation_pct',
            new_name='PM25_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='SO2_cost_escalation_pct',
            new_name='SO2_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='elec_cost_escalation_pct',
            new_name='elec_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='microgrid_upgrade_cost_pct',
            new_name='microgrid_upgrade_cost_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='offtaker_discount_pct',
            new_name='offtaker_discount_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='offtaker_tax_pct',
            new_name='offtaker_tax_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='om_cost_escalation_pct',
            new_name='om_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='owner_discount_pct',
            new_name='owner_discount_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='owner_tax_pct',
            new_name='owner_tax_rate_fraction',
        ),
        migrations.RenameField(
            model_name='generatorinputs',
            old_name='federal_itc_pct',
            new_name='federal_itc_fraction',
        ),
        migrations.RenameField(
            model_name='generatorinputs',
            old_name='fuel_renewable_energy_pct',
            new_name='fuel_renewable_energy_fraction',
        ),
        migrations.RenameField(
            model_name='generatorinputs',
            old_name='macrs_bonus_pct',
            new_name='macrs_bonus_fraction',
        ),
        migrations.RenameField(
            model_name='generatorinputs',
            old_name='min_turn_down_pct',
            new_name='min_turn_down_fraction',
        ),
        migrations.RenameField(
            model_name='generatorinputs',
            old_name='state_ibi_pct',
            new_name='state_ibi_fraction',
        ),
        migrations.RenameField(
            model_name='generatorinputs',
            old_name='utility_ibi_pct',
            new_name='utility_ibi_fraction',
        ),
        migrations.RenameField(
            model_name='pvinputs',
            old_name='degradation_pct',
            new_name='degradation_fraction',
        ),
        migrations.RenameField(
            model_name='pvinputs',
            old_name='federal_itc_pct',
            new_name='federal_itc_fraction',
        ),
        migrations.RenameField(
            model_name='pvinputs',
            old_name='macrs_bonus_pct',
            new_name='macrs_bonus_fraction',
        ),
        migrations.RenameField(
            model_name='pvinputs',
            old_name='operating_reserve_required_pct',
            new_name='operating_reserve_required_fraction',
        ),
        migrations.RenameField(
            model_name='pvinputs',
            old_name='state_ibi_pct',
            new_name='state_ibi_fraction',
        ),
        migrations.RenameField(
            model_name='pvinputs',
            old_name='utility_ibi_pct',
            new_name='utility_ibi_fraction',
        ),
        migrations.RenameField(
            model_name='siteinputs',
            old_name='CO2_emissions_reduction_max_pct',
            new_name='CO2_emissions_reduction_max_fraction',
        ),
        migrations.RenameField(
            model_name='siteinputs',
            old_name='CO2_emissions_reduction_min_pct',
            new_name='CO2_emissions_reduction_min_fraction',
        ),
        migrations.RenameField(
            model_name='siteinputs',
            old_name='renewable_electricity_max_pct',
            new_name='renewable_electricity_max_fraction',
        ),
        migrations.RenameField(
            model_name='siteinputs',
            old_name='renewable_electricity_min_pct',
            new_name='renewable_electricity_min_fraction',
        ),
        migrations.RenameField(
            model_name='siteoutputs',
            old_name='lifecycle_emissions_reduction_CO2_pct',
            new_name='lifecycle_emissions_reduction_CO2_fraction',
        ),
        migrations.RenameField(
            model_name='siteoutputs',
            old_name='renewable_electricity_pct',
            new_name='renewable_electricity_fraction',
        ),
        migrations.RenameField(
            model_name='siteoutputs',
            old_name='renewable_electricity_pct_bau',
            new_name='renewable_electricity_fraction_bau',
        ),
        migrations.RenameField(
            model_name='siteoutputs',
            old_name='total_renewable_energy_pct',
            new_name='total_renewable_energy_fraction',
        ),
        migrations.RenameField(
            model_name='siteoutputs',
            old_name='total_renewable_energy_pct_bau',
            new_name='total_renewable_energy_fraction_bau',
        ),
        migrations.RenameField(
            model_name='windinputs',
            old_name='federal_itc_pct',
            new_name='federal_itc_fraction',
        ),
        migrations.RenameField(
            model_name='windinputs',
            old_name='macrs_bonus_pct',
            new_name='macrs_bonus_fraction',
        ),
        migrations.RenameField(
            model_name='windinputs',
            old_name='operating_reserve_required_pct',
            new_name='operating_reserve_required_fraction',
        ),
        migrations.RenameField(
            model_name='windinputs',
            old_name='state_ibi_pct',
            new_name='state_ibi_fraction',
        ),
        migrations.RenameField(
            model_name='windinputs',
            old_name='utility_ibi_pct',
            new_name='utility_ibi_fraction',
        ),
        migrations.AlterField(
            model_name='electricloadoutputs',
            name='critical_load_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, help_text='Hourly critical load for outage simulator. Values are either uploaded by user, or determined from typical load (either uploaded or simulated) and critical_load_fraction.', size=None),
        ),
        migrations.AlterField(
            model_name='financialoutputs',
            name='microgrid_upgrade_cost',
            field=models.FloatField(blank=True, help_text='Cost to make a distributed energy system islandable from the grid. Determined by multiplying the total capital costs of resultant energy systems from REopt (such as PV and Storage system) with the input value for microgrid_upgrade_cost_fraction (which defaults to 0.30).', null=True),
        ),
    ]
