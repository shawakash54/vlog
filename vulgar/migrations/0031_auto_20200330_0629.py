# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-30 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0030_language_is_default'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='language',
            managers=[
                ('published_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='published_status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=100),
        ),
    ]
