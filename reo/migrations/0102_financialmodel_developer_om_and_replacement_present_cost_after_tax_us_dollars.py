# Generated by Django 2.2.13 on 2021-02-16 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0101_auto_20210127_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialmodel',
            name='developer_om_and_replacement_present_cost_after_tax_us_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
