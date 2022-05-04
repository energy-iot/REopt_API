# Generated by Django 4.0.2 on 2022-04-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_boilerinputs_fuel_cost_per_mmbtu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boilerinputs',
            name='fuel_type',
            field=models.TextField(blank=True, choices=[('natural_gas', 'Natural Gas'), ('landfill_bio_gas', 'Landfill Bio Gas'), ('propane', 'Propane'), ('diesel_oil', 'Diesel Oil'), ('uranium', 'Uranium')], default='natural_gas'),
        ),
    ]
