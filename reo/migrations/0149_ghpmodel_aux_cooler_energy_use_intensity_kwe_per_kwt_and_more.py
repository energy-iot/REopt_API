# Generated by Django 4.0.7 on 2023-02-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0148_alter_electrictariffmodel_coincident_peak_load_active_timesteps'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghpmodel',
            name='aux_cooler_energy_use_intensity_kwe_per_kwt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpmodel',
            name='aux_cooler_installed_cost_us_dollars_per_ton',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpmodel',
            name='aux_heater_installed_cost_us_dollars_per_mmbtu_per_hr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpmodel',
            name='aux_heater_thermal_efficiency',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpmodel',
            name='aux_heater_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ghpmodel',
            name='is_hybrid_ghx',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
