from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from vulgar.models import BlogLanguage
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils.html import escape
from django.utils.timezone import get_current_timezone


class PoliticsPostsFeed(Feed):
    language_code = 'EN'
    title = "Politics"
    # link = "/politics/"
    description = "Latest news and breaking stories on Indian and West Bengal politics. Find updates, comment and expert analysis on government policies and bills | TrikonIndia"
    days = 7

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='politics', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=self.days), \
            language__code=self.language_code)

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/politics/'

    def link(self, obj):
        return f'https://trikonindia.com/politics/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class PoliticsPostsFeedHindi(PoliticsPostsFeed):
    language_code = 'HI'
    title = "राजनीति"
    description = "भारतीय और पश्चिम बंगाल की राजनीति पर नवीनतम समाचार और ब्रेकिंग कहानियां। सरकारी नीतियों और बिलों पर अपडेट, टिप्पणी और विशेषज्ञ विश्लेषण का पता लगाएं।"

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/hi/politics/'

    def link(self, obj):
        return f'https://trikonindia.com/hi/politics/'


class PoliticsPostsFeedBengali(PoliticsPostsFeed):
    language_code = 'BN'
    title = "রাজনীতি"
    description = "ভারতীয় এবং পশ্চিমবঙ্গ রাজনীতির সর্বশেষ সংবাদ এবং ব্রেকিং গল্প। সরকারী নীতি এবং বিলে আপডেট, মন্তব্য এবং বিশেষজ্ঞ বিশ্লেষণ সন্ধান করুন।"
    days = 15

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/bn/politics/'

    def link(self, obj):
        return f'https://trikonindia.com/bn/politics/'


class TechnologyPostsFeed(Feed):
    language_code = 'EN'
    title = "Technology"
    # link = "/technology/"
    description = "Latest Technology News and Daily Updates on TrikonIndia. Get trending tech news, mobile phones, laptops, reviews, software updates, video games, internet and other technology updates on gadgets from India and around the world. | TrikonIndia"
    days = 7

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='technology', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=self.days), \
            language__code=self.language_code)
    
    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/technology/'

    def link(self, obj):
        return f'https://trikonindia.com/technology/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class TechnologyPostsFeedHindi(TechnologyPostsFeed):
    language_code = 'HI'
    title = "टैकनोलजी"
    description = "TrikonIndia पर नवीनतम प्रौद्योगिकी समाचार और दैनिक अपडेट। भारत और दुनिया भर के गैजेट्स पर ट्रेंडिंग टेक न्यूज़, मोबाइल फोन, लैपटॉप, रिव्यू, सॉफ्टवेयर अपडेट, वीडियो गेम, इंटरनेट और अन्य टेक्नोलॉजी अपडेट प्राप्त करें।"

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/hi/technology/'

    def link(self, obj):
        return f'https://trikonindia.com/hi/technology/'


class TechnologyPostsFeedBengali(TechnologyPostsFeed):
    language_code = 'BN'
    title = "প্রযুক্তি"
    description = "TrikonIndia সর্বশেষ প্রযুক্তির সংবাদ এবং দৈনিক আপডেট ates ভারত এবং বিশ্বের বিভিন্ন গ্যাজেটগুলির ট্রেন্ডিং টেক নিউজ, মোবাইল ফোন, ল্যাপটপ, পর্যালোচনা, সফ্টওয়্যার আপডেট, ভিডিও গেমস, ইন্টারনেট এবং অন্যান্য প্রযুক্তি আপডেট পান।"
    days = 15

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/bn/technology/'

    def link(self, obj):
        return f'https://trikonindia.com/bn/technology/'


class SportsPostsFeed(Feed):
    language_code = 'EN'
    title = "Sports"
    # link = "/sports/"
    description = "Sports News - Read Latest Sports News Today Headlines on TrikonIndia.com. Find latest cricket news, tennis, football, hockey, World cup 2019, IPL 2020 Live Score Updates. Stay updated on Sports News. Get West Bengal sports updates. Get India sports updates. | TrikonIndia"
    days = 7

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='sports', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=self.days),\
            language__code=self.language_code)

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/sports/'

    def link(self, obj):
        return f'https://trikonindia.com/sports/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class SportsPostsFeedHindi(SportsPostsFeed):
    language_code = 'HI'
    title = "खेल"
    description = "खेल समाचार - TrikonIndia.com पर नवीनतम खेल समाचार आज की सुर्खियाँ पढ़ें। नवीनतम क्रिकेट समाचार, टेनिस, फुटबॉल, हॉकी, विश्व कप 2019, आईपीएल 2020 लाइव स्कोर अपडेट प्राप्त करें। स्पोर्ट्स न्यूज पर अपडेट रहें। पश्चिम बंगाल खेल अद्यतन प्राप्त करें। भारत खेल अद्यतन प्राप्त करें।"

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/hi/sports/'

    def link(self, obj):
        return f'https://trikonindia.com/hi/sports/'


class SportsPostsFeedBengali(SportsPostsFeed):
    language_code = 'BN'
    title = "স্পোর্টস"
    description = "স্পোর্টস নিউজ - TrikonIndia ডটকমের সর্বশেষ স্পোর্টস নিউজ টুডে শিরোনামগুলি পড়ুন। সর্বশেষ ক্রিকেটের সংবাদ, টেনিস, ফুটবল, হকি, বিশ্বকাপ 2019, আইপিএল 2020 লাইভ স্কোর আপডেটগুলি সন্ধান করুন। স্পোর্টস নিউজে আপডেট থাকুন। পশ্চিমবঙ্গের ক্রীড়া আপডেট পান। ভারতের ক্রীড়া আপডেট পান।"
    days = 15

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/bn/sports/'

    def link(self, obj):
        return f'https://trikonindia.com/bn/sports/'


class HealthPostsFeed(Feed):
    language_code = 'EN'
    title = "Health"
    # link = "/health/"
    description = "Medical news and health news headlines posted throughout the day, every day - India, West Bengal. | TrikonIndia"
    days = 7

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='health', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=self.days), \
            language__code=self.language_code)

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/health/'

    def link(self, obj):
        return f'https://trikonindia.com/health/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class HealthPostsFeedHindi(HealthPostsFeed):
    language_code = 'HI'
    title = "स्वास्थ्य"
    description = "चिकित्सा समाचार और स्वास्थ्य समाचार दिन भर में पोस्ट होते हैं, हर दिन - भारत, पश्चिम बंगाल।"

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/hi/health/'

    def link(self, obj):
        return f'https://trikonindia.com/hi/health/'


class HealthPostsFeedBengali(HealthPostsFeed):
    language_code = 'BN'
    title = "স্বাস্থ্য"
    description = "মেডিকেল সংবাদ এবং স্বাস্থ্য খবরের শিরোনাম দিনব্যাপী প্রতিদিন পোস্ট করা হয় - ভারত, পশ্চিমবঙ্গ।"
    days = 15

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/bn/health/'

    def link(self, obj):
        return f'https://trikonindia.com/bn/health/'


class EconomyPostsFeed(Feed):
    language_code = 'EN'
    title = "Economy"
    # link = "/economy/"
    description = "Business News - Read Latest Financial news, Stock/Share Market News, Economy News, Business News. Find IPO Analysis, Mutual Funds Trends & Analysis, Gold Rate, Real Estate & more. | TrikonIndia"
    days = 7

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='economy', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=self.days), \
            language__code=self.language_code)

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/economy/'

    def link(self, obj):
        return f'https://trikonindia.com/economy/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class EconomyPostsFeedHindi(EconomyPostsFeed):
    language_code = 'HI'
    title = "इकॉनमी"
    description = "व्यावसायिक समाचार - नवीनतम वित्तीय समाचार, स्टॉक / शेयर बाजार समाचार, अर्थव्यवस्था समाचार, व्यवसाय समाचार पढ़ें। आईपीओ विश्लेषण, म्युचुअल फंड रुझान और विश्लेषण, गोल्ड रेट, रियल एस्टेट और अधिक जानकारी प्राप्त करें।"

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/hi/economy/'

    def link(self, obj):
        return f'https://trikonindia.com/hi/economy/'


class EconomyPostsFeedBengali(EconomyPostsFeed):
    language_code = 'BN'
    title = "ইকোনমি"
    description = "বিজনেস নিউজ - সর্বশেষ আর্থিক সংবাদ, স্টক / শেয়ার মার্কেট নিউজ, ইকোনমি নিউজ, বিজনেস নিউজ পড়ুন। আইপিও বিশ্লেষণ, মিউচুয়াল ফান্ডের প্রবণতা ও বিশ্লেষণ, সোনার হার, রিয়েল এস্টেট এবং আরও অনেক কিছু পান।"
    days = 15

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/bn/economy/'

    def link(self, obj):
        return f'https://trikonindia.com/bn/economy/'


class EntertainmentPostsFeed(Feed):
    language_code = 'EN'
    title = "Entertainment"
    # link = "/entertainment/"
    description = "Latest entertainment news and gossip from the world of bollywood, Hollywood and regional film industries. Get the latest celebrity news on celebrity scandals, engagements, and divorces. Get latest updates on nepotism, inside knowledge of bollywood and hollywood industry. | TrikonIndia"
    days = 7

    def items(self):
        return BlogLanguage.published_objects.filter(blog__primary_category__slug='entertainment', \
            created_at__gte=datetime.now(tz=get_current_timezone())-timedelta(days=self.days), \
            language__code=self.language_code)

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/entertainment/'

    def link(self, obj):
        return f'https://trikonindia.com/entertainment/'

    def item_title(self, item):
        return escape(item.title)

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return f'https://trikonindia.com/{item.language.slug}/{item.blog.primary_category.slug}/{item.blog.slug}/'


class EntertainmentPostsFeedHindi(EntertainmentPostsFeed):
    language_code = 'HI'
    title = "मनोरंजन"
    description = "बॉलीवुड, हॉलीवुड और क्षेत्रीय फिल्म उद्योगों की दुनिया से नवीनतम मनोरंजन समाचार और गपशप। सेलिब्रिटी घोटालों, सगाई और तलाक पर नवीनतम सेलिब्रिटी समाचार प्राप्त करें। बॉलीवुड और हॉलीवुड उद्योग के ज्ञान के अंदर भाई-भतीजावाद पर नवीनतम अपडेट प्राप्त करें।"

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/hi/entertainment/'

    def link(self, obj):
        return f'https://trikonindia.com/hi/entertainment/'


class EntertainmentPostsFeedBengali(EntertainmentPostsFeed):
    language_code = 'BN'
    title = "বিনোদন"
    description = "বলিউড, হলিউড এবং আঞ্চলিক ফিল্ম ইন্ডাস্ট্রির বিশ্বের সর্বশেষ বিনোদন সংবাদ এবং গসিপ। সেলিব্রিটি কেলেঙ্কারী, বাগদান এবং বিবাহবিচ্ছেদের বিষয়ে সর্বশেষ খ্যাতির খবর পান। বলিউড এবং হলিউড শিল্পের অভ্যন্তরীণ জ্ঞান, নেপোটিজম সম্পর্কিত সর্বশেষ আপডেট পান।"
    days = 15

    def feed_url(self, obj):
        return f'https://trikonindia.com/feed/bn/entertainment/'

    def link(self, obj):
        return f'https://trikonindia.com/bn/entertainment/'