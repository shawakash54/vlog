# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-25 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0016_blog_meta_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='meta_keywords',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=50), size=None), blank=True, null=True, size=None),
        ),
    ]
