# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 12:10
from __future__ import unicode_literals

from django.db import migrations

def generate_language_display_name(apps, schema_editor):
    Language = apps.get_model('vulgar', 'Language')
    display_name_hash = {
        'EN': 'English',
        'HI': 'हिन्दी',
        'BN': 'বাংলা',
        'AS': 'অসমীয়া',
        'GU': 'ગુજરાતી',
        'KN': 'ಕನ್ನಡ',
        'ML': 'മലയാളം',
        'MR': 'मराठी',
        'NE': 'नेपाली',
        'OR': 'ओड़िया',
        'PA': 'ਪੰਜਾਬੀ',
        'SD': 'سنڌي',
        'TA': 'தமிழ்',
        'TE': 'తెలుగు',
        'UR': 'اردو',
        'BH': 'बिहारी'
    }
    for language in Language.objects.all():
        language.display_name = display_name_hash.get(language.code)
        language.save()

class Migration(migrations.Migration):

    dependencies = [
        ('vulgar', '0008_auto_20200530_1209'),
    ]

    operations = [
        migrations.RunPython(generate_language_display_name),
    ]
