from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import vulgar.models as vulgar_models
import vulgar.constants as vulgar_contants


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        active_languages = vulgar_models.Language.published_objects.all()
        urls = ['about-us', 'contact-us']
        items_list = []
        for url in urls:
            items_list.append(f'/{url}/')
        for url in urls:
            for active_language in active_languages:
                items_list.append(f'/{active_language.slug}/{url}/')
        return items_list

    def location(self, item):
        return item


class HomePage_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        items_list = []
        active_languages = vulgar_models.Language.published_objects.all()
        items_list.append('/')
        for active_language in active_languages:
            items_list.append(f'/{active_language.slug}/')
        return items_list

    def location(self, item):
        return item


class Category_Sitemap_Localized(Sitemap):

    changefreq = "daily"
    priority = 1.0
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        return vulgar_models.CategoryLanguage.published_objects.all()

    def location(self, obj):
        return '/' + obj.language.slug + '/' + obj.category.slug + '/'

    def lastmod(self, obj): 
        return obj.updated_at


class Category_Sitemap(Sitemap):

    changefreq = "daily"
    priority = 1.0
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        return vulgar_models.Category.published_objects.all()

    def location(self, obj):
        return '/' + obj.slug + '/'

    def lastmod(self, obj): 
        return obj.updated_at


class Article_Sitemap(Sitemap):

    changefreq = "daily"
    priority = 1.0
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        list_urls = []
        for blog in vulgar_models.Blog.published_objects.all():
            default_blog_language = vulgar_models.BlogLanguage.published_objects.filter(blog=blog, language__slug='en').last()
            blog_languages = vulgar_models.BlogLanguage.published_objects.filter(blog=blog)
            blog_ob = {
                'instance': default_blog_language,
                'url': f'/topic/{blog.slug}/'
            }
            list_urls.append(blog_ob.copy())
            for blog_language in blog_languages:
                blog_ob_new = {}
                blog_ob_new['instance'] = blog_language
                blog_ob_new['url'] = f'/{blog_language.language.slug}/topic/{blog.slug}/'
                list_urls.append(blog_ob_new.copy())
            for category in blog.category.all():
                blog_ob['url'] = f'/{category.slug}/{blog.slug}/'
                list_urls.append(blog_ob.copy())
                for blog_language in blog_languages:
                    blog_ob_new = {}
                    blog_ob_new['instance'] = blog_language
                    blog_ob_new['url'] = f'/{blog_language.language.slug}/{category.slug}/{blog.slug}/'
                    list_urls.append(blog_ob_new.copy())
        print(list_urls)
        return list_urls

    def location(self, obj):
        return obj.get('url')

    def lastmod(self, obj): 
        return obj.get('instance').updated_at