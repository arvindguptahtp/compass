# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 12:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20170608_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='assessment_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='program',
            name='gender',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='grade',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='is_cost_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='program',
            name='outcomes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='race',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='region',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='service_categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='setting',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='student_characteristics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='student_need',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='tiers_of_evidence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='program',
            name='tiers_of_service',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
    ]
