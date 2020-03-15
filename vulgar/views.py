from django.views.generic import TemplateView
from django.template.response import TemplateResponse
import vulgar.models as vulgar_models

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['categories'] = vulgar_models.Category.objects.filter(home_page_view=True)
        context['trending'] = vulgar_models\
                                    .Tag.objects.filter(name__icontains='Trending').first()\
                                    .blogs.all().select_related()\
                                    .order_by('-created_at')[:5]
        context['recent'] = vulgar_models\
                                    .Tag.objects.filter(name__icontains='Recent').first()\
                                    .blogs.all().select_related()\
                                    .order_by('-created_at')[:5]
        context['special'] = vulgar_models\
                                    .Tag.objects.filter(name__icontains='Special').first()\
                                    .blogs.all().select_related()\
                                    .order_by('-created_at')[:5]                                    
        return context


class CategoryPageView(TemplateView):
    template_name = "category.html"

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.get_template_name(*args, **kwargs),
                                self.get_context_data(*args, **kwargs))

    def get_template_name(self, *args, **kwargs):
        template_name = self.template_name
        slug = kwargs.get('slug', None)
        category = vulgar_models.Category.objects.filter(slug=slug)
        if not category:
            template_name = '404.html'
        return template_name

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryPageView, self).get_context_data(*args, **kwargs)
        slug = kwargs.get('slug', None)
        category = vulgar_models.Category.objects.filter(slug=slug).select_related().first()
        context['categories'] = vulgar_models.Category.objects.filter(home_page_view=True)
        context['category'] = category
        return context


class PostPageView(TemplateView):
    template_name = "post.html"

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.get_template_name(*args, **kwargs),
                                self.get_context_data(*args, **kwargs))

    def get_template_name(self, *args, **kwargs):
        template_name = self.template_name
        slug = kwargs.get('slug', None)
        blog = vulgar_models.Blog.objects.filter(slug=slug)
        if not blog:
            template_name = '404.html'
        return template_name

    def get_context_data(self, *args, **kwargs):
        context = super(PostPageView, self).get_context_data(*args, **kwargs)
        slug = kwargs.get('slug', None)
        blog = vulgar_models.Blog.objects.filter(slug=slug).select_related().first()
        context['categories'] = vulgar_models.Category.objects.filter(home_page_view=True)
        context['blog'] = blog
        return context