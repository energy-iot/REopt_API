# Generated by Django 4.0.7 on 2024-02-10 18:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0039_boilerinputs_boileroutputs_steamturbineinputs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='existingboilerinputs',
            name='fuel_renewable_energy_fraction',
            field=models.FloatField(blank=True, help_text='Fraction of the fuel considered renewable. Default depends on fuel type.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='chpinputs',
            name='emissions_factor_lb_CO2_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='chpinputs',
            name='emissions_factor_lb_NOx_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='chpinputs',
            name='emissions_factor_lb_PM25_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='chpinputs',
            name='emissions_factor_lb_SO2_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of CO2 emitted per MMBTU of CHP fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='chpinputs',
            name='fuel_renewable_energy_fraction',
            field=models.FloatField(blank=True, help_text='Fraction of the CHP fuel considered renewable. Default depends on fuel type.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='electricutilityinputs',
            name='cambium_location_type',
            field=models.TextField(blank=True, default='GEA Regions', help_text="Geographic boundary at which emissions are calculated. Options: ['Nations', 'GEA Regions', 'States']."),
        ),
        migrations.AlterField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_CO2_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of CO2e emitted per MMBTU of fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
        migrations.AlterField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_NOx_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of NOx emitted per MMBTU of fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
        migrations.AlterField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_PM25_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of PM2.5 emitted per MMBTU fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
        migrations.AlterField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_SO2_per_mmbtu',
            field=models.FloatField(blank=True, help_text='Pounds of SO2 emitted per MMBTU of fuel burned.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
    ]
