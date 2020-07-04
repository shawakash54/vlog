from django.db.models.signals import post_save
from vulgar.models import BlogLanguage
import requests
from datetime import datetime, timedelta
import random
import json

headers = {
    'webpushrKey': 'Fu9VxIHQXEsXtGDRIn6zQZFN35KxqAbEXXl4qUoIy-A',
    'webpushrAuthToken': '9106',
    'Content-Type': 'application/json',
}


def blog_language_web_push(sender, instance, created, **kwargs):
    if created and instance.language.code == 'EN':
        english_primary_category_language = instance.blog.primary_category.categorylanguage_set.all().filter(language__code='EN').last()
        notification_time = datetime.now() - timedelta(hours=5, minutes=30) + timedelta(minutes=random.randint(10, 50))
        # notification_time = datetime.now() + timedelta(minutes=1) 
        blog_language_url = f'https://trikonindia.com/en/{english_primary_category_language.category.slug}/{instance.blog.slug}'

        related_news_url = f'https://trikonindia.com/en/{english_primary_category_language.category.slug}'
        data = {
            "title": instance.title,
            "message": instance.description[:120] + '..',
            "target_url": blog_language_url,
            "name": instance.title + '-' + instance.language.code,
            "icon": "https://trikonindia-assets.s3.amazonaws.com/media/trikonindia.png",
            "image": instance.blog.hero_image.url,
            "send_at": notification_time.isoformat(),
            "action_buttons": [
                {
                    "title": "Related News",
                    "url": related_news_url
                },
                {
                    "title": "Politics",
                    "url": f'https://trikonindia.com/en/politics'
                }
            ]
        }
        print(f'Data for campaign: {data}')
        response = requests.post('https://api.webpushr.com/v1/notification/send/all', headers=headers, data=json.dumps(data))
        print(f'campaign created: {response.ok} {response.json().get("ID")}')

    if created and instance.language.code == 'BN' and len(instance.blog.bloglanguage_set.all()) == 3:
        notification_time = datetime.now() - timedelta(hours=5, minutes=30) + timedelta(minutes=random.randint(10, 50))
        # notification_time = datetime.now() + timedelta(minutes=1) 
        english_blog_langugae = instance.blog.bloglanguage_set.all().filter(language__code='EN').last()
        english_blog_language_url = f'https://trikonindia.com/en/{instance.blog.primary_category.slug}/{instance.blog.slug}'
        hindi_blog_language_url = f'https://trikonindia.com/hi/{instance.blog.primary_category.slug}/{instance.blog.slug}'
        bengali_blog_language_url = f'https://trikonindia.com/bn/{instance.blog.primary_category.slug}/{instance.blog.slug}'
        data = {
            "title": english_blog_langugae.title,
            "message": english_blog_langugae.description[:120] + '..',
            "target_url": english_blog_language_url,
            "name": 'multilanguage-target-' + english_blog_langugae.title + '-' + english_blog_langugae.language.code,
            "icon": "https://trikonindia-assets.s3.amazonaws.com/media/trikonindia.png",
            "image": english_blog_langugae.blog.hero_image.url,
            "send_at": notification_time.isoformat(),
            "action_buttons": [
                {
                    "title": "Bengali",
                    "url": bengali_blog_language_url
                },
                {
                    "title": "Hindi",
                    "url": hindi_blog_language_url
                }
            ]
        }
        print(f'Data for multi language campaign: {data}')
        response = requests.post('https://api.webpushr.com/v1/notification/send/all', headers=headers, data=json.dumps(data))
        print(f'multi language campaign created: {response.ok} {response.json().get("ID")}')


post_save.connect(blog_language_web_push, sender=BlogLanguage)