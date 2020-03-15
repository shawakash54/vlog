# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-14 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vulgar.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=100000)),
                ('published_status', models.CharField(choices=[(vulgar.models.PublishedStatusChoice('Draft'), 'Draft'), (vulgar.models.PublishedStatusChoice('Active'), 'Active'), (vulgar.models.PublishedStatusChoice('Inactive'), 'Inactive')], max_length=100)),
                ('published_date_from', models.DateTimeField()),
                ('published_date_to', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('published_status', models.CharField(choices=[(vulgar.models.PublishedStatusChoice('Draft'), 'Draft'), (vulgar.models.PublishedStatusChoice('Active'), 'Active'), (vulgar.models.PublishedStatusChoice('Inactive'), 'Inactive')], max_length=100)),
                ('published_date_from', models.DateTimeField()),
                ('published_date_to', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vulgar.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vulgar.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vulgar.Page'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vulgar.Tag'),
        ),
    ]
