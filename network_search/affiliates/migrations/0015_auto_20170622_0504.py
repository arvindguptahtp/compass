# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0014_excelupload_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate',
            name='address_state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='excelupload',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
