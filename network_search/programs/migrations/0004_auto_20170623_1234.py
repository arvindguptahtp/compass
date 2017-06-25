# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20170618_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalResource',
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
        migrations.AddField(
            model_name='program',
            name='program_weblink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='additionalresource',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_resources', to='programs.Program'),
        ),
    ]