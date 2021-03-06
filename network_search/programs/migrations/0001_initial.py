# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 21:21
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('affiliates', '0001_initial'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, help_text='Optional visible for link', max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=400)),
                ('search_content', django.contrib.postgres.search.SearchVectorField()),
                ('summary', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('grade', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('gender', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('race', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('region', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('student_need', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('student_characteristics', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('tiers_of_service', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('setting', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('tiers_of_evidence', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('service_categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('assessment_available', models.BooleanField()),
                ('assessment_info', models.CharField(blank=True, max_length=400, null=True)),
                ('is_cost_free', models.BooleanField()),
                ('cost_description', models.CharField(blank=True, max_length=200, null=True)),
                ('outcomes', models.TextField(blank=True)),
                ('study_weblink', models.URLField(blank=True, null=True)),
                ('featured_network', models.ManyToManyField(blank=True, help_text="This is populated by first selecting affiliates for 'Network Use' and saving.", related_name='featured_programs', to='affiliates.Affiliate')),
                ('national_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program', to='partners.Partner')),
                ('network_use', models.ManyToManyField(blank=True, related_name='programs', to='affiliates.Affiliate')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('programs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RelatedResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, help_text='Optional visible for link', max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_resources', to='programs.Program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='nationaldatabase',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_databases', to='programs.Program'),
        ),
    ]
