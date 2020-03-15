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
from vulgar.views import HomePageView, CategoryPageView, PostPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^(?P<slug>[-\w]+)$', CategoryPageView.as_view()),
    url(r'^topic/(?P<slug>[\w-]+)/$', PostPageView.as_view()),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
