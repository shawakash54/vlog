from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import vulgar.models as vulgar_models
import vulgar.constants as vulgar_contants


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        return ['contact_us_view', 'about_us_view']

    def location(self, item):
        return reverse(item) + '/'


class HomePage_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'
    protocol = vulgar_contants.URL_PROTOCOL

    def items(self):
        return ['home_page_view']

    def location(self, item):
        return reverse(item)


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
            blog_ob = {
                'instance': blog,
                'url': f'/topic/{blog.slug}/'
            }
            list_urls.append(blog_ob.copy())
            for category in blog.category.all():
                blog_ob['url'] = f'/{category.slug}/{blog.slug}/'
                list_urls.append(blog_ob.copy())
        return list_urls

    def location(self, obj):
        return obj.get('url')

    def lastmod(self, obj): 
        return obj.get('instance').updated_at