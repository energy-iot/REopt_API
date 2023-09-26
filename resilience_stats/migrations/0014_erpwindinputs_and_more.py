# Generated by Django 4.0.4 on 2023-09-19 21:31

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import resilience_stats.models


class Migration(migrations.Migration):

    dependencies = [
        ('resilience_stats', '0013_alter_erpelectricstorageinputs_num_battery_bins'),
    ]

    operations = [
        migrations.CreateModel(
            name='ERPWindInputs',
            fields=[
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ERPWindInputs', serialize=False, to='resilience_stats.erpmeta')),
                ('operational_availability', models.FloatField(blank=True, default=0.97, help_text='Fraction of the year that the wind system is not down for maintenance', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)])),
                ('size_kw', models.FloatField(blank=True, default=0.0, help_text='Wind system capacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)])),
                ('production_factor_series', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]), blank=True, default=list, help_text='Wind system output at each timestep, normalized to wind system size. Must be hourly (8,760 samples).', size=None)),
            ],
            bases=(resilience_stats.models.BaseModel, models.Model),
        ),
        migrations.AlterField(
            model_name='erpelectricstorageinputs',
            name='operational_availability',
            field=models.FloatField(blank=True, default=0.97, help_text='Fraction of the year that the battery system is not down for maintenance', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='erpgeneratorinputs',
            name='operational_availability',
            field=models.FloatField(blank=True, default=0.995, help_text='Fraction of the year that each generator unit is not down for maintenance', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='erpprimegeneratorinputs',
            name='operational_availability',
            field=models.FloatField(blank=True, help_text='Fraction of the year that each prime generator/CHP unit is not down for maintenance', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='erppvinputs',
            name='operational_availability',
            field=models.FloatField(blank=True, default=0.98, help_text='Fraction of the year that the PV system is not down for maintenance', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
