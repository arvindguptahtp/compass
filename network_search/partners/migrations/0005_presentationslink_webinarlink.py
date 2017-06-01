# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_remove_partner_webinars'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentationsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presentations', to='partners.Partner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WebinarLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webinars', to='partners.Partner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]