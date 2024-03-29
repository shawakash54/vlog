# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-20 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0010_auto_20200320_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='breadcrumb_title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='blog',
            name='primary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vulgar.Category'),
        ),
    ]
