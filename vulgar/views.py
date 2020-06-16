from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from rest_framework.response import Response
import vulgar.models as vulgar_models
from django.shortcuts import render
import vulgar.serializers as vulgar_serializers
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404, HttpResponse
import vulgar.utils as vulgar_utils
import vulgar.constants as vulgar_constants
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET
import itertools
import random
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        language_code = self.request.LANGUAGE_CODE
        context['canonical_link'] = vulgar_utils.form_canonical_url('home_page', None)
        context['alternate_language'] = vulgar_utils.get_alternate_language('home_page', None)
        context['categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                    category__home_page_view=True,
                                    language__slug=language_code
                                ).select_related('category', 'language')
        context['meta'] = vulgar_utils.get_meta_info('home_page', None, language_code)
        context['trending_blog_languages'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Trending').first()\
                                    .blogs.filter(language__slug=language_code)\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )\
                                    .order_by('-created_at')[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['recent_blog_languages'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Recent').first()\
                                    .blogs.filter(language__slug=language_code)\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )\
                                    .order_by('-created_at')[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['politics_category_language'], context['politics_category_blog_languages'] = self.get_category_blogs('politics', language_code)
        context['economy_category_language'], context['economy_category_blog_languages'] = self.get_category_blogs('economy', language_code)
        context['sports_category_language'], context['sports_category_blog_languages'] = self.get_category_blogs('sports', language_code)
        context['sexual_wellness_category_language'], context['sexual_wellness_category_blog_languages'] = self.get_category_blogs('sexual-wellness', language_code)
        context['entertainment_category_language'], context['entertainment_category_blog_languages'] = self.get_category_blogs('entertainment', language_code)
        context['health_category_language'], context['health_category_blog_languages'] = self.get_category_blogs('health', language_code)
        context['special_blog_languages'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Special').first()\
                                    .blogs.filter(language__slug=language_code)\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )\
                                    .order_by('-created_at')[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['highlighted_blog_languages'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Highlighted').first()\
                                    .blogs.filter(language__slug=language_code)\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )\
                                    .order_by('-created_at')[:2],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['dmiss_blog_languages'] = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains="Don't Miss").first()\
                                    .blogs.filter(language__slug=language_code)\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )\
                                    .order_by('-created_at')[:2],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['constants'] = vulgar_constants
        context['social_meta_tags'] = vulgar_utils.get_social_media_meta_tags('home_page', None, language_code, context['categories_languages'])
        return context

    def get_category_blogs(self, category_slug, language_code):
        category = vulgar_models.CategoryLanguage.published_objects.filter(
                    category__slug=category_slug,
                    language__slug=language_code
                ).last()
        category_blogs = vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models.BlogLanguage\
                                    .published_objects\
                                    .filter(
                                        blog__category__categorylanguage=category,
                                        language__slug=language_code
                                    )\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )[:5],
                                many=True,
                                context={'language_code': language_code}
                            ).data
        return [category, category_blogs]
        


class CategoryPageView(TemplateView):
    template_name = "category.html"

    def get(self, request, *args, **kwargs):
        status, template_name, category_language = self.get_template_name(*args, **kwargs)
        page_number = int(request.GET.get('page', 1))
        return TemplateResponse(request, template_name,
                                self.get_context_data(category_language, page_number, *args, **kwargs), status=status)

    def get_template_name(self, *args, **kwargs):
        template_name = self.template_name
        status = 200
        slug = kwargs.get('slug', None)
        language_code = self.request.LANGUAGE_CODE
        category_language = None
        category_language = vulgar_models.CategoryLanguage.published_objects.filter(
                                    category__slug=slug,
                                    language__slug=language_code
                                ).select_related('category', 'language').last()
        if not category_language:
            status = 404
            template_name = 'error.html'
        return (status, template_name, category_language)

    def get_context_data(self, category_language, page_number, *args, **kwargs):
        context = super(CategoryPageView, self).get_context_data(*args, **kwargs)
        slug = kwargs.get('slug', None)
        language_code = self.request.LANGUAGE_CODE
        context['categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                    category__home_page_view=True,
                                    language__slug=language_code
                                )
        context['category_language'] = vulgar_serializers.CategoryLanguageSerializer(category_language, context={
                                                                                                            'language_code': language_code,
                                                                                                            'page_number': page_number
                                                                                                        }).data
        context['constants'] = vulgar_constants
        if not category_language:
            context['message'] = 'The page you are looking for was not found.'
            context['status'] = '404'
            vulgar_utils.log_missing(text = slug, model_type = vulgar_models.CategoryLanguage)
        else:
            context['canonical_link'] = vulgar_utils.form_canonical_url('category_page', category_language, language_code)
            context['meta'] = vulgar_utils.get_meta_info('category_page', category_language, language_code)
            context['alternate_language'] = vulgar_utils.get_alternate_language('category_page', category_language)
            context['social_meta_tags'] = vulgar_utils.get_social_media_meta_tags('category_page', category_language, language_code)
            context['category_blogs'] = context['category_language'].get('blogs')
            context['page_number'] = page_number
        return context


class PostPageView(TemplateView):
    template_name = "post.html"

    def get(self, request, *args, **kwargs):
        status, template_name, blog_language = self.get_template_name(*args, **kwargs)
        return TemplateResponse(request, template_name,
                                self.get_context_data(blog_language, *args, **kwargs), status=status)

    def get_template_name(self, *args, **kwargs):
        language_code = self.request.LANGUAGE_CODE
        template_name = self.template_name
        status = 200
        slug = kwargs.get('slug', None)
        category_slug = kwargs.get('category_slug', None)
        blog_language = None
        if category_slug is None :
            blog_language = vulgar_models.BlogLanguage.published_objects.filter(
                                blog__slug=slug,
                                language__slug=language_code
                            ).select_related('blog', 'language', 'creator', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user').last()
        else :
            blog_language = vulgar_models.BlogLanguage.published_objects.filter(
                                blog__slug=slug,
                                language__slug=language_code,
                                blog__category__slug=category_slug
                            ).select_related('blog', 'language', 'creator', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user').last()
        if not blog_language:
            status = 404
            template_name = 'error.html'
        return (status, template_name, blog_language)

    def get_context_data(self, blog_language, *args, **kwargs):
        language_code = self.request.LANGUAGE_CODE
        context = super(PostPageView, self).get_context_data(*args, **kwargs)
        context['categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                            category__home_page_view=True,
                                            language__slug=language_code
                                        ).select_related('category', 'language')
        slug = kwargs.get('slug', None)
        category_slug = kwargs.get('category_slug', None)
        if category_slug is None :
            present_primary_category = blog_language.blog.primary_category
            present_category_language = vulgar_models.CategoryLanguage.published_objects.filter(
                                            category=present_primary_category,
                                            language__slug=language_code
                                        ).select_related('category', 'language', 'category__image', 'category__social_media_image').last()
        else :
            present_category_language = vulgar_models.CategoryLanguage.published_objects.filter(
                                            category__slug=category_slug,
                                            language__slug=language_code
                                        ).select_related('category', 'language', 'category__image', 'category__social_media_image').last()
        context['constants'] = vulgar_constants
        if blog_language and present_category_language:
            context['all_categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(language__slug=language_code)
            context['blog_language'] =   vulgar_serializers.BlogLanguageSerializer(\
                                    blog_language,
                                    context={'language_code': language_code}
                                ).data
            context['present_category_language'] = present_category_language
            context['tags'] = blog_language.tags.all()
            context['popular_blogs_langugaes'] = self.get_popular_blogs(slug, language_code)
            context['related_blogs_languages'] = self.get_related_blogs(blog_language, language_code)
            context['canonical_link'] = vulgar_utils.form_canonical_url('article_page', blog_language, language_code)
            context['meta'] = vulgar_utils.get_meta_info('article_page', blog_language, language_code)
            context['alternate_language'] = vulgar_utils.get_alternate_language('article_page', blog_language)
            context['social_meta_tags'] = vulgar_utils.get_social_media_meta_tags('article_page', blog_language, language_code)
            context['background_image'] = f'images/background-image-{self.generate_random_number(1,10)}.jpeg'
            context['share_this_display'] = True
        else:
            context['message'] = 'The page you are looking for was not found.'
            context['status'] = '404'
            vulgar_utils.log_missing(text = slug, model_type = vulgar_models.BlogLanguage)
        return context

    def generate_random_number(self, a, b):
        if b is None:
            a, b = 0, a
        return random.randint(a, b)

    def get_popular_blogs(self, slug, language_code):
        return vulgar_serializers.BlogLanguageSerializer(\
                                vulgar_models\
                                    .Tag.published_objects.filter(name__icontains='Popular').first()\
                                    .blogs.filter(language__slug=language_code)\
                                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                                    .prefetch_related('language__country', 'tags', 'blog__category', )\
                                    .order_by('-created_at')[:4],
                                many=True,
                                context={'language_code': language_code}
                            ).data


    def get_related_blogs(self, blog_language, language_code):
        categories = blog_language.blog.category.all()[:4]
        related_blogs_languages = []
        for category in categories:
            blog_language_obj = vulgar_serializers.BlogLanguageSerializer(\
                        vulgar_models.BlogLanguage.published_objects.filter(
                            language__slug=language_code,
                            blog__category=category,
                            ).exclude(blog__slug=blog_language.blog.slug)\
                            .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                            .prefetch_related('language__country', 'tags', 'blog__category', )\
                            .order_by('-created_at')[:4],
                        many=True,
                        context={'language_code': language_code}
                    ).data
            related_blogs_languages.append(blog_language_obj)
        return list(itertools.chain.from_iterable(related_blogs_languages))


class AboutUsPageView(TemplateView):
    template_name = "pages/about-us.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUsPageView, self).get_context_data(*args, **kwargs)
        language_code = self.request.LANGUAGE_CODE
        context['categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                            category__home_page_view=True,
                                            language__slug=language_code
                                        )
        context['canonical_link'] = vulgar_utils.form_canonical_url('about_us')
        context['meta'] = vulgar_utils.get_meta_info('about_us', None)
        context['constants'] = vulgar_constants
        context['alternate_language'] = vulgar_utils.get_alternate_language('about_us', None)
        context['social_meta_tags'] = vulgar_utils.get_social_media_meta_tags('about_us', None, language_code)
        return context


def DisplayContactUsPage(request):
    context = {}
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
    else:
        language_code = request.LANGUAGE_CODE
        context['categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                            category__home_page_view=True,
                                            language__slug=language_code
                                        )
        context['alternate_language'] = vulgar_utils.get_alternate_language('contact_us', None)
        context['social_meta_tags'] = vulgar_utils.get_social_media_meta_tags('contact_us', None, language_code)
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
    status = 404

    def get_context_data(self, *args, **kwargs):
        context = super(NotFoundView, self).get_context_data(*args, **kwargs)
        context['message'] = _('The page you are looking for was not found.')
        context['status'] = '404'
        context['constants'] = vulgar_constants
        return context


class SearchPageView(TemplateView):
    template_name = "searchpage.html"

    def get(self, request, *args, **kwargs):
        status, template_name = self.get_template_name(*args, **kwargs)
        search_query = request.GET.get('search', '')
        return TemplateResponse(request, template_name,
                                self.get_context_data(search_query, *args, **kwargs), status=status)

    def get_template_name(self, *args, **kwargs):
        template_name = self.template_name
        status = 200
        return (status, template_name)

    def get_context_data(self, search_query, *args, **kwargs):
        language_code = self.request.LANGUAGE_CODE
        context = super(SearchPageView, self).get_context_data(*args, **kwargs)
        search_query_length = len(search_query)
        similarity_threshold = 0.3
        if search_query_length < 5:
            similarity_threshold = 0.05
        elif search_query_length < 10:
            similarity_threshold = 0.1
        elif search_query_length < 15:
            similarity_threshold = 0.2
        blogs = vulgar_models.BlogLanguage.published_objects.annotate(
                    similarity=TrigramSimilarity('title', search_query)
                ).filter(similarity__gt=similarity_threshold, language__slug=language_code).order_by('-similarity')\
                .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                    'blog__hero_image', 'blog__thumbnail_image', \
                    'blog__social_media_image', 'creator__auth_user', )\
                .prefetch_related('language__country', 'tags', 'blog__category', )[:12]
        context['blogs'] = vulgar_serializers.BlogLanguageSerializer(\
                                blogs,
                                many=True,
                                context={'language_code': language_code}
                            ).data
        context['constants'] = vulgar_constants
        context['categories_languages'] = vulgar_models.CategoryLanguage.published_objects.filter(
                                    category__home_page_view=True,
                                    language__slug=language_code
                                ).select_related('category', 'language')
        context['alternate_language'] = vulgar_utils.get_alternate_language('search_page', search_query)    
        context['meta'] = vulgar_utils.get_meta_info('search_page', search_query, language_code)  
        context['canonical_link'] = vulgar_utils.form_canonical_url('search_page', search_query, language_code)
        context['social_meta_tags'] = vulgar_utils.get_social_media_meta_tags('search_page', search_query, language_code)                      
        return context


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "",
        vulgar_utils.get_sitemap_url(),
        vulgar_utils.get_host_url()
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


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

