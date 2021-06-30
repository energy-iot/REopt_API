# Generated by Django 3.1.12 on 2021-06-29 22:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0111_auto_20210524_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadprofileboilerfuelmodel',
            name='addressable_fraction',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, null=True, size=None),
        ),
    ]
