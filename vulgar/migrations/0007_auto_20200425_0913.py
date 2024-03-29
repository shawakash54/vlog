# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0006_auto_20200425_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='social_media_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogs_social_media', to='vulgar.Media'),
        ),
        migrations.AddField(
            model_name='category',
            name='social_media_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories_social_media', to='vulgar.Media'),
        ),
        migrations.AlterField(
            model_name='mediatype',
            name='media_type',
            field=models.CharField(choices=[('document', 'document'), ('image', 'image'), ('video', 'video')], db_index=True, max_length=100),
        ),
    ]
