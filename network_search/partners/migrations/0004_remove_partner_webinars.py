# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 15:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_partner_webinars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='webinars',
        ),
    ]