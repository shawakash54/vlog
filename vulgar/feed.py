from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from vulgar.models import BlogLanguage
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils.html import escape
from django.utils.timezone import get_current_timezone


class PoliticsPostsFeed(Feed):
    title = "Politics"
    # link = "/politics/"
    description = "Latest news and breaking stories on Indian and West Bengal politics. Find updates, comment and expert analysis on government policies and bills | TrikonIndia"

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='politics', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=5))

    def link(self, obj):
        return f'https://trikonindia.com/politics/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class TechnologyPostsFeed(Feed):
    title = "Technology"
    # link = "/technology/"
    description = "Latest Technology News and Daily Updates on TrikonIndia. Get trending tech news, mobile phones, laptops, reviews, software updates, video games, internet and other technology updates on gadgets from India and around the world. | TrikonIndia"

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='technology', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=5))

    def link(self, obj):
        return f'https://trikonindia.com/technology/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class SportsPostsFeed(Feed):
    title = "sports"
    # link = "/sports/"
    description = "Sports News - Read Latest Sports News Today Headlines on TrikonIndia.com. Find latest cricket news, tennis, football, hockey, World cup 2019, IPL 2020 Live Score Updates. Stay updated on Sports News. Get West Bengal sports updates. Get India sports updates. | TrikonIndia"

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='sports', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=5))

    def link(self, obj):
        return f'https://trikonindia.com/sports/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class HealthPostsFeed(Feed):
    title = "health"
    # link = "/health/"
    description = "Medical news and health news headlines posted throughout the day, every day - India, West Bengal. | TrikonIndia"

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='health', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=5))

    def link(self, obj):
        return f'https://trikonindia.com/health/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class EconomyPostsFeed(Feed):
    title = "economy"
    # link = "/economy/"
    description = "Business News - Read Latest Financial news, Stock/Share Market News, Economy News, Business News. Find IPO Analysis, Mutual Funds Trends & Analysis, Gold Rate, Real Estate & more. | TrikonIndia"

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='economy', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=5))

    def link(self, obj):
        return f'https://trikonindia.com/economy/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class EntertainmentPostsFeed(Feed):
    title = "entertainment"
    # link = "/entertainment/"
    description = "Latest entertainment news and gossip from the world of bollywood, Hollywood and regional film industries. Get the latest celebrity news on celebrity scandals, engagements, and divorces. Get latest updates on nepotism, inside knowledge of bollywood and hollywood industry. | TrikonIndia"

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='entertainment', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=5))

    def link(self, obj):
        return f'https://trikonindia.com/entertainment/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'