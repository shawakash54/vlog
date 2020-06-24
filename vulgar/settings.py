"""
Django settings for vulgar project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _
from decouple import config as decouple_config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = decouple_config('SECRET_KEY', '343##$$NDWDIENVINIVNIEINVINEINVIENIVN2323')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = decouple_config('DEBUG', False, cast=bool)


ALLOWED_HOSTS = [decouple_config('HOST', '127.0.0.1')]

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'flat_responsive', # only if django version < 2.0
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_extensions',
    'storages',
    'vulgar',
    'ckeditor',
    'rest_framework',
    'django_bootstrap_breadcrumbs',
    'cities_light',
    'django_better_admin_arrayfield',
    'bulk_admin',
    'searchableselect',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'vulgar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + "/vlog-templates/"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
USE_S3 = decouple_config('USE_S3', "False") == 'True'

if USE_S3:
    # aws settings
    AWS_S3_ACCESS_KEY_ID = decouple_config('AWS_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY = decouple_config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = decouple_config('AWS_STORAGE_BUCKET_NAME')
    AWS_PRELOAD_METADATA = True
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'vulgar.storage_backends.StaticStorage'
    # STATICFILES_STORAGE = 'myproject.storage.S3Storage'
    # s3 public media settings
    # STATIC_URL = '/static/'
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'vulgar.storage_backends.PublicMediaStorage'
    # AWS_S3_SECURE_URLS = False
    AWS_S3_REGION_NAME = "ap-south-1"
    AWS_S3_SIGNATURE_VERSION = "s3v4"
    AWS_S3_ADDRESSING_STYLE = "path"
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, './vlog-templates/'),
]

WSGI_APPLICATION = 'vulgar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': decouple_config('VULGAR_DB_NAME', 'vulgar'),
        'USER': decouple_config('VULGAR_DB_USER', 'vulgar'),
        'PASSWORD': decouple_config('VULGAR_DB_PASSWORD', 'vulgar'),
        'HOST': decouple_config('VULGAR_DB_HOST', 'localhost'),
        'PORT': decouple_config('VULGAR_DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 500,
        'width': 1000,
    },
}

BREADCRUMBS_TEMPLATE = "components/breadcrumbs.html"

# LANGUAGES = [
#     ('en', _('English')),
#     ('ur', _('Urdu')),
#     ('ne', _('Nepali')),
#     ('te', _('Telugu')),
#     ('ta', _('Tamil')),
#     ('pa', _('Punjabi')),
#     ('mr', _('Marathi')),
#     ('ml', _('Malayalam')),
#     ('kn', _('Kannada')),
#     ('bn', _('Bengali')),
#     ('hi', _('Hindi')),
# ]
LANGUAGES = [
    ('en', _('English')),
    ('hi', _('Hindi')),
    ('bn', _('Bengali')),
]
LANGUAGE_CODE = 'en'

LOCALE_PATHS = [ os.path.join(BASE_DIR, 'locale'), ]


CITIES_LIGHT_INCLUDE_COUNTRIES = ['IN']

if DEBUG:
    # Django Debug Toolbar
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
    }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': decouple_config('LOG_DIRECTORY', os.path.join(BASE_DIR, "./logs")) + "/django-logs",
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
