# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0017_auto_20170623_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooleoydata',
            name='cis_model_school',
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='location_model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_grade_12_deceased',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_grade_12_expelled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_grade_12_ged',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_grade_12_incarcerated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_k_11_deceased',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_k_11_expelled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_k_11_ged',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schooleoydata',
            name='students_k_11_incarcerated',
            field=models.IntegerField(default=0),
        ),
    ]
