# Generated by Django 4.0.7 on 2023-03-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0151_remove_ghpmodel_aux_cooler_energy_use_intensity_kwe_per_kwt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghpmodel',
            name='aux_unit_capacity_sizing_factor_on_peak_load',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
