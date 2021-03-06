# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0002_auto_20170608_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affiliate',
            options={'verbose_name': 'Affiliate', 'verbose_name_plural': 'Affiliates'},
        ),
        migrations.AlterModelOptions(
            name='affiliateeoydata',
            options={'verbose_name': 'Affiliate EOY Data', 'verbose_name_plural': 'Affiliate EOY Data'},
        ),
        migrations.AlterModelOptions(
            name='endofyear',
            options={'ordering': ['-year_ends'], 'verbose_name': 'Reporting Year', 'verbose_name_plural': 'Reporting Years'},
        ),
        migrations.AlterModelOptions(
            name='schooleoydata',
            options={'verbose_name': 'School EOY Data', 'verbose_name_plural': 'School EOY Data'},
        ),
        migrations.AlterModelOptions(
            name='studenteoydata',
            options={'verbose_name': 'Student EOY Data', 'verbose_name_plural': 'Student EOY Data'},
        ),
    ]
