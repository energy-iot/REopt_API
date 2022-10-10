# Generated by Django 4.0.6 on 2022-10-10 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_messagesoutputs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electricstorageinputs',
            name='installed_cost_per_kw',
            field=models.FloatField(blank=True, default=775.0, help_text='Total upfront battery power capacity costs (e.g. inverter and balance of power systems)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='electricstorageinputs',
            name='installed_cost_per_kwh',
            field=models.FloatField(blank=True, default=388.0, help_text='Total upfront battery costs', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='electricstorageinputs',
            name='replace_cost_per_kw',
            field=models.FloatField(blank=True, default=440.0, help_text='Battery power capacity replacement cost at time of replacement year', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='electricstorageinputs',
            name='replace_cost_per_kwh',
            field=models.FloatField(blank=True, default=220.0, help_text='Battery energy capacity replacement cost at time of replacement year', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000.0)]),
        ),
        migrations.AlterField(
            model_name='financialinputs',
            name='elec_cost_escalation_pct',
            field=models.FloatField(blank=True, default=0.019, help_text='Annual nominal utility electricity cost escalation rate.', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='financialinputs',
            name='offtaker_discount_pct',
            field=models.FloatField(blank=True, default=0.0564, help_text='Nominal energy offtaker discount rate. In single ownership model the offtaker is also the generation owner.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='financialinputs',
            name='owner_discount_pct',
            field=models.FloatField(blank=True, default=0.0564, help_text='Nominal generation owner discount rate. Used for two party financing model. In two party ownership model the offtaker does not own the generator(s).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='pvinputs',
            name='installed_cost_per_kw',
            field=models.FloatField(blank=True, default=1592, help_text='Installed PV cost in $/kW', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AlterField(
            model_name='pvinputs',
            name='om_cost_per_kw',
            field=models.FloatField(blank=True, default=17, help_text='Annual PV operations and maintenance costs in $/kW', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000.0)]),
        ),
        migrations.AlterField(
            model_name='windinputs',
            name='om_cost_per_kw',
            field=models.FloatField(blank=True, default=35, help_text='Annual operations and maintenance costs in $/kW', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000.0)]),
        ),
    ]
