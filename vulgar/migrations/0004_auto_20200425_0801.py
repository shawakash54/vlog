# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0003_auto_20200425_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hero_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='thumbnail_image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
