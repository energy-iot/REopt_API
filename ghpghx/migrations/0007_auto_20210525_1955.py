# Generated by Django 3.1.8 on 2021-05-25 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghpghx', '0006_auto_20210525_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghpghxmodel',
            name='ground_thermal_conductivity_btu_per_hr_ft_f',
            field=models.FloatField(blank=True, default=1.18, help_text='Thermal conductivity of the ground surrounding the borehole field [Btu/(hr-ft-degF)]', null=True, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(15.0)]),
        ),
        migrations.AlterField(
            model_name='ghpghxmodel',
            name='solver_eft_tolerance_f',
            field=models.FloatField(blank=True, default=2.0, help_text='Tolerance for GHX sizing based on the entering fluid temperature limits [degF]', null=True, validators=[django.core.validators.MinValueValidator(0.001), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
