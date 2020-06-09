from rest_framework import serializers
from vulgar.models import Feedback, NewsLetterSubscription, BlogLanguage, CategoryLanguage, Blog, User
from django.conf import settings
from django.contrib.auth.models import User as AuthUser


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class NewsLetterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterSubscription
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('slug', 'hero_image', 'thumbnail_image', 'primary_category')
        depth = 1


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('first_name', 'last_name', 'email', 'username')


class UserSerializer(serializers.ModelSerializer):
    auth_user = AuthUserSerializer()
    class Meta:
        model = User
        fields = ('bio', 'auth_user')


class BlogLanguageSerializer(serializers.ModelSerializer):
    present_category_language = serializers.SerializerMethodField('category_language')
    created_at = serializers.SerializerMethodField()
    blog = BlogSerializer()
    creator = UserSerializer()

    class Meta:
        model = BlogLanguage
        fields = ('blog', 'creator', 'language', 'title', 'breadcrumb_title', 'tags', 'description', 'content', 'present_category_language', 'created_at')
        depth = 1

    def category_language(self, model_obj):
        language_code = self.context.get("language_code")
        categories = model_obj.blog.category.all()
        category_language = CategoryLanguage.published_objects.filter(
            category__in=categories,
            language__slug = language_code
        )
        return category_language

    def get_created_at(self, model_obj):
        return model_obj.created_at.date


class CategoryLanguageSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField('category_language_slug')
    created_at = serializers.SerializerMethodField()
    blogs = serializers.SerializerMethodField('category_language_blogs')
    # category_image = serializers.SerializerMethodField('category_language_image')

    class Meta:
        model = CategoryLanguage
        fields = ('category_description', 'name', 'slug', 'breadcrumb_title', 'created_at', 'blogs')
        depth = 1

    def category_language_slug(self, model_obj):
        return model_obj.category.slug

    def category_language_image(self, model_obj):
        return model_obj.category.image.url

    def category_language_blogs(self, model_obj):
        language_code = self.context.get("language_code")
        blogs = BlogLanguage\
                    .published_objects\
                    .filter(
                        blog__category__categorylanguage=model_obj,
                        language__slug=language_code
                    )\
                    .select_related('language', 'creator', 'blog', 'blog__primary_category', \
                                                    'blog__hero_image', 'blog__thumbnail_image', \
                                                    'blog__social_media_image', 'creator__auth_user', )\
                    .prefetch_related('language__country', 'tags', 'blog__category', )
        return BlogLanguageSerializer(blogs,
                                many=True,
                                context={'language_code': language_code}
                            ).data

    def get_created_at(self, model_obj):
        return model_obj.created_at.date