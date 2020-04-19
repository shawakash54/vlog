# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-30 05:52
from __future__ import unicode_literals

from django.db import migrations

def migrate_data(apps, schema_editor):
    Language = apps.get_model('vulgar', 'Language')
    Category = apps.get_model('vulgar', 'Category')
    Tag = apps.get_model('vulgar', 'Tag')
    Blog = apps.get_model('vulgar', 'Blog')
    CategoryLanguage = apps.get_model('vulgar', 'CategoryLanguage')
    BlogLanguage = apps.get_model('vulgar', 'BlogLanguage')

    englishLanguage = Language.objects.filter(name='English').last()

    for category in Category.published_objects.all():
        categoryLanguage = CategoryLanguage(
            category = category,
            language = englishLanguage,
            name = category.name,
            meta_keywords = category.meta_keywords,
            meta_description = category.meta_description,
            category_description = category.category_description
        )
        categoryLanguage.save()

    
    for blog in Blog.published_objects.all():
        blogLanguage = BlogLanguage(
            blog = blog,
            language = englishLanguage,
            title = blog.title,
            breadcrumb_title = blog.breadcrumb_title,
            meta_keywords = blog.meta_keywords,
            meta_description = blog.meta_description,
            description = blog.description,
            content = blog.content,
            creator = blog.creator
        )
        blogLanguage.save()
        

    for tag in Tag.published_objects.all():
        tag.language = englishLanguage
        tag.save()


class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0027_auto_20200330_0549'),
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
