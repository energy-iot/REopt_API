# Generated by Django 2.2.13 on 2021-01-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0078_auto_20201231_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrictariffmodel',
            name='total_coincident_peak_cost_bau_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='total_coincident_peak_cost_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_coincident_peak_cost_bau_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_coincident_peak_cost_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
