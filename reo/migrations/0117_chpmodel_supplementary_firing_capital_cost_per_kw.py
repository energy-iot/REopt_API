# Generated by Django 3.1.12 on 2021-09-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0116_auto_20210818_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='chpmodel',
            name='supplementary_firing_capital_cost_per_kw',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
