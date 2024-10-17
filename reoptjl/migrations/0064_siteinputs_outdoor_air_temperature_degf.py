# Generated by Django 4.0.7 on 2024-09-10 01:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0063_ghpoutputs_thermal_to_dhw_load_series_mmbtu_per_hour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinputs',
            name='outdoor_air_temperature_degF',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text="The outdoor air (dry-bulb) temperature in degrees Fahrenheit as determined by the site's location TMY3 data from the PVWatts call or user input. This is used for GHP COP and ASHP COP and CF values based on the default or custom mapping of those.", size=None),
        ),
    ]