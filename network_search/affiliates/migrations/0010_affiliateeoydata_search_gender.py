# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:43
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0009_schooleoydata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliateeoydata',
            name='search_gender',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
    ]
