# Generated by Django 4.0.7 on 2024-08-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0060_processheatloadinputs_addressable_load_fraction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioUnlinkedRuns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_uuid', models.UUIDField()),
                ('user_uuid', models.UUIDField()),
                ('run_uuid', models.UUIDField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='apimeta',
            name='portfolio_uuid',
            field=models.TextField(blank=True, default='', help_text='The unique ID of a portfolio (set of associated runs) created by the REopt Webtool. Note that this ID can be shared by several REopt API Scenarios and one user can have one-to-many portfolio_uuid tied to them.'),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='reopt_version',
            field=models.TextField(blank=True, default='', help_text='Version number of the Julia package for REopt that is used to solve the problem.', null=True),
        ),
    ]
