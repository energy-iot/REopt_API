# Generated by Django 4.0.4 on 2023-01-03 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resilience_stats', '0013_alter_erpgeneratorinputs_failure_to_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erpprimegeneratorinputs',
            name='mean_time_to_failure',
            field=models.FloatField(blank=True, help_text="Average number of time steps between a prime generator/CHP unit's failures. 1/(failure to run probability).", null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
