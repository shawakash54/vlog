# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-21 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0002_auto_20200616_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='published_date_from',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='published_date_to',
        ),
    ]
