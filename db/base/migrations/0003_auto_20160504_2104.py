# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150908_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemodData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.PositiveIntegerField()),
                ('payload', jsonfield.fields.JSONField(default=dict)),
                ('transmitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Transmitter')),
            ],
        ),
        migrations.AddField(
            model_name='satellite',
            name='telemetry_decoder',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='satellite',
            name='telemetry_schema',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
    ]
