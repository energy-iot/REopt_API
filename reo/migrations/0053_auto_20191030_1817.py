# REopt®, Copyright (c) Alliance for Sustainable Energy, LLC. See also https://github.com/NREL/REopt_API/blob/master/LICENSE.
# Generated by Django 2.2.6 on 2019-10-30 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0052_auto_20191030_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='parse_run_outputs_seconds2',
            new_name='parse_run_outputs_seconds',
        ),
        migrations.RenameField(
            model_name='profilemodel',
            old_name='pre_setup_scenario_seconds2',
            new_name='pre_setup_scenario_seconds',
        ),
        migrations.RenameField(
            model_name='profilemodel',
            old_name='reopt_bau_seconds2',
            new_name='reopt_bau_seconds',
        ),
        migrations.RenameField(
            model_name='profilemodel',
            old_name='reopt_seconds2',
            new_name='reopt_seconds',
        ),
        migrations.RenameField(
            model_name='profilemodel',
            old_name='setup_scenario_seconds2',
            new_name='setup_scenario_seconds',
        ),
    ]
