# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0007_auto_20170619_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='affiliateeoydata',
            old_name='school_districts',
            new_name='districts',
        ),
    ]
