# Generated by Django 4.0.6 on 2022-08-11 01:18

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_electrictariffinputs_coincident_peak_load_active_timesteps_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolingLoadInputs',
            fields=[
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='CoolingLoadInputs', serialize=False, to='job.apimeta')),
                ('doe_reference_name', models.TextField(blank=True, choices=[('FastFoodRest', 'Fastfoodrest'), ('FullServiceRest', 'Fullservicerest'), ('Hospital', 'Hospital'), ('LargeHotel', 'Largehotel'), ('LargeOffice', 'Largeoffice'), ('MediumOffice', 'Mediumoffice'), ('MidriseApartment', 'Midriseapartment'), ('Outpatient', 'Outpatient'), ('PrimarySchool', 'Primaryschool'), ('RetailStore', 'Retailstore'), ('SecondarySchool', 'Secondaryschool'), ('SmallHotel', 'Smallhotel'), ('SmallOffice', 'Smalloffice'), ('StripMall', 'Stripmall'), ('Supermarket', 'Supermarket'), ('Warehouse', 'Warehouse'), ('FlatLoad', 'Flatload'), ('FlatLoad_24_5', 'Flatload 24 5'), ('FlatLoad_16_7', 'Flatload 16 7'), ('FlatLoad_16_5', 'Flatload 16 5'), ('FlatLoad_8_7', 'Flatload 8 7'), ('FlatLoad_8_5', 'Flatload 8 5')], help_text="Building type to use in selecting a simulated load profile from DOE <a href='https: //energy.gov/eere/buildings/commercial-reference-buildings' target='blank'>Commercial Reference Buildings</a>.By default, the doe_reference_name of the ElectricLoad is used.")),
                ('blended_doe_reference_names', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, choices=[('FastFoodRest', 'Fastfoodrest'), ('FullServiceRest', 'Fullservicerest'), ('Hospital', 'Hospital'), ('LargeHotel', 'Largehotel'), ('LargeOffice', 'Largeoffice'), ('MediumOffice', 'Mediumoffice'), ('MidriseApartment', 'Midriseapartment'), ('Outpatient', 'Outpatient'), ('PrimarySchool', 'Primaryschool'), ('RetailStore', 'Retailstore'), ('SecondarySchool', 'Secondaryschool'), ('SmallHotel', 'Smallhotel'), ('SmallOffice', 'Smalloffice'), ('StripMall', 'Stripmall'), ('Supermarket', 'Supermarket'), ('Warehouse', 'Warehouse'), ('FlatLoad', 'Flatload'), ('FlatLoad_24_5', 'Flatload 24 5'), ('FlatLoad_16_7', 'Flatload 16 7'), ('FlatLoad_16_5', 'Flatload 16 5'), ('FlatLoad_8_7', 'Flatload 8 7'), ('FlatLoad_8_5', 'Flatload 8 5')]), blank=True, default=list, help_text='Used in concert with blended_doe_reference_percents to create a blended load profile from multiple DoE Commercial Reference Buildings.', size=None)),
                ('blended_doe_reference_percents', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]), blank=True, default=list, help_text='Used in concert with blended_doe_reference_names to create a blended load profile from multiple DoE Commercial Reference Buildings to simulate buildings/campuses. Must sum to 1.0.', size=None)),
                ('annual_tonhour', models.FloatField(blank=True, help_text="Annual electric chiller energy consumption, in [Ton-Hours],used to scale simulated default electric chiller load profile for the site's climate zone", null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000.0)])),
                ('monthly_tonhour', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)]), blank=True, default=list, help_text="Monthly site space cooling requirement in [Ton-Hour], used to scale simulated default building load profile for the site's climate zone", size=None)),
                ('thermal_loads_ton', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Typical electric chiller load for all hours in one year. Must be hourly (8,760 samples), 30 minute (17,520 samples), or 15 minute (35,040 samples).', size=None)),
                ('annual_fraction_of_electric_load', models.FloatField(blank=True, help_text="Annual electric chiller energy consumption scalar (i.e. fraction of total electric load)used to scale simulated default electric chiller load profile for the site's climate zone", null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('monthly_fractions_of_electric_load', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]), blank=True, default=list, help_text="Monthly fraction of site's total electric consumption used up by electric chiller.to scale simulated default building load profile for the site's climate zone", size=None)),
                ('per_time_step_fractions_of_electric_load', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text="Per timestep fraction of site's total electric consumption used up by electric chiller.Must be hourly (8,760 samples), 30 minute (17,520 samples), or 15 minute (35,040 samples).", size=None)),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='ExistingChillerInputs',
            fields=[
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ExistingChillerInputs', serialize=False, to='job.apimeta')),
                ('loads_kw_thermal', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, size=None)),
                ('cop', models.FloatField(blank=True, help_text='Existing electric chiller system coefficient of performance (ability to convert electricity to usable cooling thermal energy', null=True, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(20)])),
                ('max_thermal_factor_on_peak_load', models.FloatField(blank=True, default=1.25, help_text='Factor on peak thermal LOAD which the electric chiller can supply', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='ExistingChillerOutputs',
            fields=[
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ExistingChillerOutputs', serialize=False, to='job.apimeta')),
                ('year_one_to_tes_series_ton', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of electric chiller thermal to cold TES [Ton]', null=True, size=None)),
                ('year_one_to_load_series_ton', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of electric chiller thermal to cooling load [Ton]', null=True, size=None)),
                ('year_one_electric_consumption_series', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), blank=True, default=list, help_text='Year one hourly time series of chiller electric consumption [kW]', null=True, size=None)),
                ('year_one_electric_consumption_kwh', models.FloatField(blank=True, help_text='Year one chiller electric consumption [kWh]', null=True)),
                ('year_one_thermal_production_tonhour', models.FloatField(blank=True, help_text='Year one chiller thermal production [Ton Hour', null=True)),
            ],
            bases=(job.models.BaseModel, models.Model),
        ),
    ]
