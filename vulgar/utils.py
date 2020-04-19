import vulgar.models as vulgar_models
from django.contrib.contenttypes.models import ContentType
import vulgar.constants as vulgar_constants
from django.utils.translation import gettext_lazy as _


def log_missing(text, model_type):
    obj, created = vulgar_models.FailedUserQuery.objects.get_or_create(search_query__iexact=text, content_type=ContentType.objects.get_for_model(model_type), defaults={
        'search_query': text,
        'content_type': ContentType.objects.get_for_model(model_type)
    })
    obj.search_count = obj.search_count + 1
    obj.save()


def home_page_canonical(obj, language_code):
    return f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/'


def about_us_canonical(obj, language_code):
    return f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/about-us/'


def contact_us_canonical(obj, language_code):
    return f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/contact-us/'


def category_page_canonical(category_language, language_code):
    return f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{category_language.category.slug}/'


def article_page_canonical(blog_language, language_code):
    return f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{blog_language.blog.primary_category.slug}/{blog_language.blog.slug}/'


def form_canonical_url(page_type, obj=None, language_code = 'en'):
    switcher = {
        'home_page': home_page_canonical,
        'about_us': about_us_canonical,
        'contact_us': contact_us_canonical,
        'category_page': category_page_canonical,
        'article_page': article_page_canonical
    }
    return switcher.get(page_type)(obj, language_code)


def home_page_meta(obj, language_code):
    categories_languages = vulgar_models.CategoryLanguage.published_objects.filter(
                                    category__home_page_view=True,
                                    language__slug=language_code
                                )
    home_page_meta_title = _("Breaking Trending News, India and World News")
    home_page_meta_description_part_1 = _("provides latest news from India and the world. Get today’s news headlines from")
    home_page_meta_description_part_2 = _("and exclusive breaking news from India.")
    home_page_keywords = _('news, live news, news in india, breaking news, today news, current news, elections, indian news, news website, politics, india news, world news, business news, bollywood news, cricket news, sports, lifestyle, gadgets, tech news, news blogs, bedroom, sexual wellness, sex, sex updates, sex news, adult, adult news')
    return {
        'title': f'{home_page_meta_title} | {vulgar_constants.APP_NAME}',
        'meta_description': f'{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}' + \
                                f' {home_page_meta_description_part_1}' + \
                                f'{", ".join(str(category.name) for category in categories_languages)}' + \
                                f' {home_page_meta_description_part_2} | {vulgar_constants.APP_NAME}',
        'google_site_verification_code': vulgar_constants.GOOGLE_SITE_VERIFICATION_CODE,
        'search_keywords': home_page_keywords
    }


def contact_us_meta(obj, language_code):
    contact_page_meta_title = _("Contact Us for publishing articles, blogs")
    contact_page_meta_description = _("Contact for publishing news. Queries around news and paid content writing")
    contact_page_keywords = _('paid article publishing, news coverage, paid content writing, content publishing, news suggestions, news area improvement')
    return {
        'title': f'{contact_page_meta_title} | {vulgar_constants.APP_NAME}',
        'meta_description': f'{contact_page_meta_description} | {vulgar_constants.APP_NAME}',
        'google_site_verification_code': vulgar_constants.GOOGLE_SITE_VERIFICATION_CODE,
        'search_keywords': contact_page_keywords
    }


def about_us_meta(obj, language_code):
    aboutus_page_meta_title = _("About Us")
    aboutus_page_meta_description = _("About Us - A Newsletter, blog, complete transparency for public interest")
    aboutus_page_keywords = _('Completely transparent newsletter, paid article writing')
    return {
        'title': f'{aboutus_page_meta_title} | {vulgar_constants.APP_NAME}',
        'meta_description': f'{aboutus_page_meta_description} | {vulgar_constants.APP_NAME}',
        'google_site_verification_code': vulgar_constants.GOOGLE_SITE_VERIFICATION_CODE,
        'search_keywords': aboutus_page_keywords
    }


def category_page_meta(category_language, language_code):
    return {
        'title': f'{category_language.name} | {vulgar_constants.APP_NAME}',
        'meta_description': f'{category_language.meta_description} | {vulgar_constants.APP_NAME}',
        'google_site_verification_code': vulgar_constants.GOOGLE_SITE_VERIFICATION_CODE,
        'search_keywords': ', '.join(category_language.meta_keywords)
    }


def article_page_meta(blog_language, language_code):
    return {
        'title': f'{blog_language.title} | {vulgar_constants.APP_NAME}',
        'meta_description': f'{blog_language.meta_description} | {vulgar_constants.APP_NAME}',
        'google_site_verification_code': vulgar_constants.GOOGLE_SITE_VERIFICATION_CODE,
        'search_keywords': ', '.join(blog_language.meta_keywords)
    }


def get_meta_info(page_type, obj=None, language_code = 'en'):
    switcher = {
        'home_page': home_page_meta,
        'about_us': about_us_meta,
        'contact_us': contact_us_meta,
        'category_page': category_page_meta,
        'article_page': article_page_meta
    }
    return switcher.get(page_type)(obj, language_code)



def home_page_alternate_language(obj):
    alternate_language = []
    active_languages = vulgar_models.Language.published_objects.all()
    for language in active_languages:
        alternate_language.append(
            {
                'code': language.slug,
                'link': f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{language.slug}/'
            }
        )
    return alternate_language


def about_us_alternate_language(obj):
    alternate_language = []
    active_languages = vulgar_models.Language.published_objects.all()
    for language in active_languages:
        alternate_language.append(
            {
                'code': language.slug,
                'link': f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{language.slug}/about-us/'
            }
        )
    return alternate_language


def contact_us_alternate_language(obj):
    alternate_language = []
    active_languages = vulgar_models.Language.published_objects.all()
    for language in active_languages:
        alternate_language.append(
            {
                'code': language.slug,
                'link': f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{language.slug}/contact-us/'
            }
        )
    return alternate_language


def category_page_alternate_language(category_language):
    alternate_language = []
    category_active_languages = vulgar_models.Language.published_objects.filter(categorylanguage__category__slug=category_language.category.slug)
    for language in category_active_languages:
        alternate_language.append(
            {
                'code': language.slug,
                'link': f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{language.slug}/{category_language.category.slug}/'
            }
        )
    return alternate_language


def article_page_alternate_language(blog_language):
    alternate_language = []
    blog_active_languages = vulgar_models.Language.published_objects.filter(bloglanguage__blog__slug=blog_language.blog.slug)
    for language in blog_active_languages:
        alternate_language.append(
            {
                'code': language.slug,
                'link': f'{vulgar_constants.URL_SCHEME}{vulgar_constants.SECOND_LEVEL_DOMAIN}{vulgar_constants.TOP_LEVEL_DOMAIN}/{language.slug}/{blog_language.blog.primary_category.slug}/{blog_language.blog.slug}/'
            }
        )
    return alternate_language


def get_alternate_language(page_type, obj=None):
    switcher = {
        'home_page': home_page_alternate_language,
        'about_us': about_us_alternate_language,
        'contact_us': contact_us_alternate_language,
        'category_page': category_page_alternate_language,
        'article_page': article_page_alternate_language
    }
    return switcher.get(page_type)(obj)