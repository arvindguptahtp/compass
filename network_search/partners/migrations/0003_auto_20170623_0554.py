# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20170614_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='network_use',
            field=models.ManyToManyField(blank=True, related_name='partner_profiles', to='affiliates.Affiliate'),
        ),
    ]
