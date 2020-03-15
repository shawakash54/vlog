from django.views.generic import TemplateView
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
        return context
