# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-16 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0005_auto_20200315_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
