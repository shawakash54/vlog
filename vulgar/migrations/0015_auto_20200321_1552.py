# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-21 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0014_faileduserquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faileduserquery',
            name='search_count',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
