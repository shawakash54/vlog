# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-25 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0017_auto_20200325_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='meta_keywords',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
    ]
