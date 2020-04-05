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
        depth = 2

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