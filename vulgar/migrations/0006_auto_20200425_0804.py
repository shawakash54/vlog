# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0005_auto_20200425_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='alt_tag',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.CharField(blank=True, db_index=True, default='', max_length=1000, null=True),
        ),
    ]
