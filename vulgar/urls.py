"""vulgar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from vulgar.views import HomePageView, CategoryPageView, PostPageView, DisplayContactUsPage, AboutUsPageView, SubscribeView, NotFoundView, server_error, not_found, permission_denied, bad_request
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from vulgar.sitemap import Static_Sitemap, HomePage_Sitemap, Category_Sitemap, Category_Sitemap_Localized, Article_Sitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _


sitemaps = {
    'homepage': HomePage_Sitemap(),
    'static': Static_Sitemap(),
    'category': Category_Sitemap(),
    'category_localized': Category_Sitemap_Localized(),
    'article': Article_Sitemap(),
}


urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^/?$', HomePageView.as_view(), name='home_page_view'),
        url(r'^i18n/', include('django.conf.urls.i18n')),
        url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
        url(r'^subscribe/?$', SubscribeView.as_view(), name='subscribe_view'),
        url(r'^about-us/?$', AboutUsPageView.as_view(), name='about_us_view'),
        url(r'^contact-us/?$', DisplayContactUsPage, name='contact_us_view'),
    ] + list(i18n_patterns(
        url(r'^/?$', HomePageView.as_view(), name='home_page_view'),
        url(r'^contact-us/?$', DisplayContactUsPage, name='contact_us_view'),
        url(r'^about-us/?$', AboutUsPageView.as_view(), name='about_us_view'),
        url(r'^(?P<slug>[-\w]+)/?$', CategoryPageView.as_view(), name='category_view'),
        url(r'^topic/(?P<slug>[\w-]+)/?$', PostPageView.as_view(), name='article_view'),
        url(r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/?$', PostPageView.as_view(), name='article_view'),
    )) + [
        # url(r'(.*)', NotFoundView.as_view()),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = not_found
handler500 = server_error
handler403 = permission_denied
handler400 = bad_request