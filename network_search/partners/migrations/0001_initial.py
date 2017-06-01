# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 15:24
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.search
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('affiliates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=400)),
                ('grade', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None)),
                ('search_content', django.contrib.postgres.search.SearchVectorField()),
                ('network_use', models.ManyToManyField(blank=True, related_name='partners', to='affiliates.Affiliate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]