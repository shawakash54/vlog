# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-21 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('vulgar', '0012_newslettersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscription',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.City'),
        ),
    ]
