# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0012_auto_20170621_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excelupload',
            old_name='result',
            new_name='status',
        ),
    ]
