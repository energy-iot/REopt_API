# Generated by Django 4.0.4 on 2022-09-27 23:26

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resilience_stats', '0009_rename_cumulative_outage_survival_probability_erpoutputs_cumulative_outage_survival_final_time_step_'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='erpinputs',
            name='starting_battery_soc_kwh',
        ),
        migrations.AddField(
            model_name='erpinputs',
            name='battery_starting_soc_kwh',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]), blank=True, default=list, help_text='Battery kWh state of charge when an outage begins, at each timestep. Must be hourly (8,760 samples).', size=None),
        ),
    ]
