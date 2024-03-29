# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-15 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='blog',
            name='hero_image',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', to='vulgar.Tag'),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail_image',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(related_name='blogs', to='vulgar.Category'),
        ),
    ]
