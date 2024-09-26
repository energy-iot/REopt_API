# Generated by Django 4.0.7 on 2024-09-09 15:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0062_ashpspaceheateroutputs_annual_electric_consumption_for_cooling_kwh_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghpoutputs',
            name='thermal_to_dhw_load_series_mmbtu_per_hour',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='ghpoutputs',
            name='thermal_to_load_series_ton',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='ghpoutputs',
            name='thermal_to_space_heating_load_series_mmbtu_per_hour',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, default=list, null=True, size=None),
        ),
    ]
