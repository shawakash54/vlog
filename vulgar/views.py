from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from rest_framework.response import Response
import vulgar.models as vulgar_models
from django.shortcuts import render
import vulgar.serializers as vulgar_serializers
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
import vulgar.utils as vulgar_utils
import vulgar.constants as vulgar_constants
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        language_code = self.request.LANGUAGE_CODE
        context['canonical_link'] = vulgar_utils.form_canonical_url('home_page', None)
        context['alternate_language'] = vulgar_utils.get_alternate_language('home_page', None)
        context['categories'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                    category__home_page_view=True,
                                    language__slug=language_code
                                )
        context['meta'] = vulgar_utils.get_meta_info('home_page', None, language_code)
        context['trending'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Trending').first()\
                                    .blogs.filter(language__slug=language_code).select_related()\
                                    .order_by('-created_at')[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['recent'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Recent').first()\
                                    .blogs.filter(language__slug=language_code).select_related()\
                                    .order_by('-created_at')[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['special'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Special').first()\
                                    .blogs.filter(language__slug=language_code).select_related()\
                                    .order_by('-created_at')[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['constants'] = vulgar_constants
        return context


class CategoryPageView(TemplateView):
    template_name = "category.html"

    def get(self, request, *args, **kwargs):
        status, template_name = self.get_template_name(*args, **kwargs)
        return TemplateResponse(request, template_name,
                                self.get_context_data(*args, **kwargs), status=status)

    def get_template_name(self, *args, **kwargs):
        template_name = self.template_name
        status = 200
        slug = kwargs.get('slug', None)
        category = vulgar_models.Category.published_objects.filter(slug=slug)
        if not category:
            status = 404
            template_name = 'error.html'
        return (status, template_name)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryPageView, self).get_context_data(*args, **kwargs)
        slug = kwargs.get('slug', None)
        category = vulgar_models.Category.published_objects.filter(slug=slug).select_related().last()
        context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
        context['category'] = category
        if not category:
            context['message'] = 'The page you are looking for was not found.'
            context['status'] = '404'
            vulgar_utils.log_missing(text = slug, model_type = vulgar_models.Category)
        context['constants'] = vulgar_constants
        context['canonical_link'] = vulgar_utils.form_canonical_url('category_page', category)
        context['meta'] = vulgar_utils.get_meta_info('category_page', category)
        return context


class PostPageView(TemplateView):
    template_name = "post.html"

    def get(self, request, *args, **kwargs):
        status, template_name = self.get_template_name(*args, **kwargs)
        return TemplateResponse(request, template_name,
                                self.get_context_data(*args, **kwargs), status=status)

    def get_template_name(self, *args, **kwargs):
        template_name = self.template_name
        status = 200
        slug = kwargs.get('slug', None)
        category_slug = kwargs.get('category_slug', None)
        if category_slug is None :
            blog_queryset = vulgar_models.Blog.published_objects.filter(slug=slug)
        else :
            blog_queryset = vulgar_models.Blog.published_objects.filter(slug=slug, category__slug=category_slug)
        if not blog_queryset:
            status = 404
            template_name = 'error.html'
        return (status, template_name)

    def get_context_data(self, *args, **kwargs):
        context = super(PostPageView, self).get_context_data(*args, **kwargs)
        context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
        slug = kwargs.get('slug', None)
        category_slug = kwargs.get('category_slug', None)
        if category_slug is None :
            blog_queryset = vulgar_models.Blog.published_objects.filter(slug=slug).select_related()
        else :
            present_category = vulgar_models.Category.published_objects.filter(slug=category_slug).last()
            blog_queryset = vulgar_models.Blog.published_objects.filter(slug=slug, category__slug=category_slug).select_related()
        if blog_queryset and present_category:
            blog = blog_queryset.last()
            context['all_categories'] = vulgar_models.Category.published_objects.filter()
            context['blog'] = blog
            context['present_category'] = present_category
            context['tags'] = vulgar_models.Tag.published_objects.filter()
            context['popular_blogs'] = self.get_popular_blogs(slug)
            context['related_blogs'] = self.get_related_blogs(blog)
            context['canonical_link'] = vulgar_utils.form_canonical_url('article_page', blog)
            context['meta'] = vulgar_utils.get_meta_info('article_page', blog)
            context['constants'] = vulgar_constants
        else:
            context['message'] = 'The page you are looking for was not found.'
            context['status'] = '404'
            vulgar_utils.log_missing(text = slug, model_type = vulgar_models.Blog)
        return context

    def get_popular_blogs(self, slug):
        return vulgar_models\
                        .Tag.published_objects.filter(name__icontains='Popular').first()\
                        .blogs.all().select_related()\
                        .order_by('-created_at')[:4]

    def get_related_blogs(self, blog):
        categories = blog.category.all()[:4]
        related_blogs = []
        for category in categories:
            blog = category.blogs.all().order_by('-created_at')[:1].first()
            related_blogs.append(blog)
        return related_blogs


class AboutUsPageView(TemplateView):
    template_name = "pages/about-us.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUsPageView, self).get_context_data(*args, **kwargs)
        context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
        context['canonical_link'] = vulgar_utils.form_canonical_url('about_us')
        context['meta'] = vulgar_utils.get_meta_info('about_us', None)
        context['constants'] = vulgar_constants
        return context


def DisplayContactUsPage(request):
    context = {}
    context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
    context['canonical_link'] = vulgar_utils.form_canonical_url('contact_us')
    context['meta'] = vulgar_utils.get_meta_info('contact_us', None)
    context['constants'] = vulgar_constants
    if request.method == "POST":
        params = {
            "first_name": request.POST.get('first_name'),
            "last_name": request.POST.get('last_name'),
            "email_id": request.POST.get('email_id'),
            "contact_number": request.POST.get('contact_number'),
            "subject": request.POST.get('subject'),
            "message": request.POST.get('message')
        }
        serializer = vulgar_serializers.FeedbackSerializer(data = params)
        if serializer.is_valid():
            serializer.save()
            context['status'] = {
                'message': 'Your Feedback has been recorded',
                'status': 'success',
                'errors': []
            }
        else:
            context['status'] = {
                'message': 'Some error occured. Please try again',
                'status': 'error',
                'errors': serializer.errors
            }
    return render(request, 'pages/contact-us.html', context)


class SubscribeView(APIView):
    """
    List all subscriptions, or create a new subscription.
    """
    # def get(self, request, format=None):
    #     subscriptions = vulgar_models.NewsLetterSubscription.objects.all()
    #     serializer = vulgar_serializers.NewsLetterSubscriptionSerializer(subscriptions, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = vulgar_serializers.NewsLetterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotFoundView(TemplateView):
    template_name = "error.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NotFoundView, self).get_context_data(*args, **kwargs)
        context['message'] = 'The page you are looking for was not found.'
        context['status'] = '404'
        context['constants'] = vulgar_constants
        return context


def server_error(request):
    context = {}
    context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
    context['message'] = 'There was some serve error. Our team is on it.'
    context['status'] = '500'
    return render(request, 'error.html', context)
 

def not_found(request):
    context = {}
    context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
    context['message'] = 'The page you are looking for was not found.'
    context['status'] = '404'
    return render(request, 'error.html', context)
 

def permission_denied(request):
    context = {}
    context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
    context['message'] = 'Looks like you are lost.'
    context['status'] = '403'
    return render(request, 'error.html', context)
 

def bad_request(request):
    context = {}
    context['categories'] = vulgar_models.Category.published_objects.filter(home_page_view=True)
    context['message'] = 'Our system did not quite understand your request.'
    context['status'] = '400'
    return render(request, 'error.html', context)

