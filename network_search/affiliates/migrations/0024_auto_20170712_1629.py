# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0023_auto_20170712_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliateeoydata',
            name='search_students_el',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='affiliateeoydata',
            name='search_students_hs',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='affiliateeoydata',
            name='search_students_ms',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
