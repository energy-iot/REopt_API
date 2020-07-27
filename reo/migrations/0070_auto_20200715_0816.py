# Generated by Django 2.2.10 on 2020-07-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0069_scenariomodel_optimality_tolerance'),
    ]

    operations = [
        migrations.AddField(
            model_name='chpmodel',
            name='om_cost_us_dollars_per_hr_per_kw_rated',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chpmodel',
            name='size_class',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='financialmodel',
            name='total_opex_costs_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='financialmodel',
            name='year_one_opex_costs_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
