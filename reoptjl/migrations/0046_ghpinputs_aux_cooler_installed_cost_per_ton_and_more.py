# Generated by Django 4.0.7 on 2023-10-02 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0045_alter_electricstorageinputs_installed_cost_per_kw_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghpinputs',
            name='aux_cooler_installed_cost_per_ton',
            field=models.FloatField(blank=True, default=400.0, help_text='Installed cost of auxiliary cooler (e.g. cooling tower) for hybrid ghx in $/ton based on peak thermal production', validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(1000000.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='aux_heater_installed_cost_per_mmbtu_per_hr',
            field=models.FloatField(blank=True, default=26000.0, help_text='Installed cost of auxiliary heater for hybrid ghx in $/MMBtu/hr based on peak thermal production.', validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(1000000.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='aux_heater_type',
            field=models.TextField(blank=True, help_text='This field only accepts "electric" as the auxillary heater type. User does not need to provide this information.', null=True),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='aux_unit_capacity_sizing_factor_on_peak_load',
            field=models.FloatField(blank=True, default=1.2, help_text='Factor on peak heating and cooling load served by the auxiliary heater/cooler used for determining heater/cooler installed capacity', validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='avoided_capex_by_ghp_present_value',
            field=models.FloatField(blank=True, default=0.0, help_text='Expected cost of HVAC upgrades avoided due to GHP tech over Financial.analysis_years', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='ghx_only_capital_cost',
            field=models.IntegerField(blank=True, help_text='Capital cost of geothermal heat exchanger which is calculated by REopt automatically. User does not need to provide this input.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='ghx_useful_life_years',
            field=models.IntegerField(blank=True, default=50, help_text='Lifetime of geothermal heat exchanger being modeled in years. This is used to calculate residual value at end of REopt analysis period. If this value is less than Financial.analysis_years, its set to Financial.analysis_years.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(75)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='installed_cost_wwhp_cooling_pump_per_ton',
            field=models.FloatField(blank=True, default=700.0, help_text='Installed WWHP cooling heat pump cost in $/ton (based on peak cooling thermal load)', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='installed_cost_wwhp_heating_pump_per_ton',
            field=models.FloatField(blank=True, default=700.0, help_text='Installed WWHP heating heat pump cost in $/ton (based on peak heating thermal load)', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='ghpinputs',
            name='is_ghx_hybrid',
            field=models.BooleanField(blank=True, help_text='REopt derived indicator for hybrid Ghx', null=True),
        ),
        migrations.AddField(
            model_name='ghpoutputs',
            name='ghx_residual_value_present_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpoutputs',
            name='size_wwhp_cooling_pump_ton',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpoutputs',
            name='size_wwhp_heating_pump_ton',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
