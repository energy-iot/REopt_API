# Generated by Django 4.0.7 on 2023-08-08 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0040_merge_20230807_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financialinputs',
            old_name='boiler_fuel_escalation_rate_fraction',
            new_name='boiler_fuel_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='chp_fuel_escalation_rate_fraction',
            new_name='chp_fuel_cost_escalation_rate_fraction',
        ),
        migrations.RenameField(
            model_name='financialinputs',
            old_name='existing_boiler_fuel_escalation_rate_fraction',
            new_name='existing_boiler_fuel_cost_escalation_rate_fraction',
        ),
    ]
