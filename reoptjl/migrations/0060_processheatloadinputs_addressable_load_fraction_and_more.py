# Generated by Django 4.0.7 on 2024-06-01 20:15

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0059_processheatloadinputs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='processheatloadinputs',
            name='addressable_load_fraction',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]), blank=True, default=list, help_text='Fraction of input fuel load which is addressable by heating technologies (default is 1.0).Can be a scalar or vector with length aligned with use of monthly_mmbtu (12) or fuel_loads_mmbtu_per_hour.', size=None),
        ),
        migrations.AddField(
            model_name='processheatloadinputs',
            name='blended_industry_reference_names',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, choices=[('Chemical', 'Chemical'), ('Warehouse', 'Warehouse'), ('FlatLoad', 'Flatload'), ('FlatLoad_24_5', 'Flatload 24 5'), ('FlatLoad_16_7', 'Flatload 16 7'), ('FlatLoad_16_5', 'Flatload 16 5'), ('FlatLoad_8_7', 'Flatload 8 7'), ('FlatLoad_8_5', 'Flatload 8 5')], null=True), blank=True, default=list, help_text='Used in concert with blended_industry_reference_percents to create a blended load profile from multiple Industrial reference facility/sector types.', size=None),
        ),
        migrations.AddField(
            model_name='processheatloadinputs',
            name='blended_industry_reference_percents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]), blank=True, default=list, help_text='Used in concert with blended_industry_reference_names to create a blended load profile from multiple Industrial reference facility/sector types. Must sum to 1.0.', size=None),
        ),
        migrations.AddField(
            model_name='processheatloadinputs',
            name='industry_reference_name',
            field=models.TextField(blank=True, choices=[('Chemical', 'Chemical'), ('Warehouse', 'Warehouse'), ('FlatLoad', 'Flatload'), ('FlatLoad_24_5', 'Flatload 24 5'), ('FlatLoad_16_7', 'Flatload 16 7'), ('FlatLoad_16_5', 'Flatload 16 5'), ('FlatLoad_8_7', 'Flatload 8 7'), ('FlatLoad_8_5', 'Flatload 8 5')], help_text='Industrial process heat load reference facility/sector type', null=True),
        ),
        migrations.AddField(
            model_name='processheatloadinputs',
            name='monthly_mmbtu',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)]), blank=True, default=list, help_text="Monthly site process heat fuel consumption in [MMbtu], used to scale simulated default building load profile for the site's climate zone", size=None),
        ),
        migrations.AlterField(
            model_name='absorptionchillerinputs',
            name='heating_load_input',
            field=models.TextField(blank=True, choices=[('DomesticHotWater', 'Domestichotwater'), ('SpaceHeating', 'Spaceheating'), ('ProcessHeat', 'Processheat')], help_text='Absorption chiller heat input - determines what heating load is added to by absorption chiller use', null=True),
        ),
        migrations.AlterField(
            model_name='processheatloadinputs',
            name='annual_mmbtu',
            field=models.FloatField(blank=True, help_text='Annual site process heat fuel consumption, used to scale simulated default industry load profile [MMBtu]', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000.0)]),
        ),
        migrations.AlterField(
            model_name='processheatloadinputs',
            name='fuel_loads_mmbtu_per_hour',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Vector of process heat fuel loads [mmbtu/hr] over one year. Must be hourly (8,760 samples), 30 minute (17,520 samples), or 15 minute (35,040 samples). All non-net load values must be greater than or equal to zero. ', size=None),
        ),
    ]
