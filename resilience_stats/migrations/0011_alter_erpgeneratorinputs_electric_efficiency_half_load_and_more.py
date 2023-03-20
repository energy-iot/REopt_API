# Generated by Django 4.0.7 on 2023-03-20 18:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resilience_stats', '0010_alter_erpelectricstorageinputs_operational_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erpgeneratorinputs',
            name='electric_efficiency_half_load',
            field=models.FloatField(blank=True, help_text='Electric efficiency of generator running at half load. Defaults to electric_efficiency_full_load', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='erpprimegeneratorinputs',
            name='electric_efficiency_half_load',
            field=models.FloatField(blank=True, help_text='Electric efficiency of prime generator/CHP unit running at half load. Defaults to electric_efficiency_full_load', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
