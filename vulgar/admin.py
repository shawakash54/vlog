from django.contrib import admin
from django.apps import apps
from django import forms
from vulgar.models import BlogLanguage, Media, CategoryLanguage, Tag, Blog
from ckeditor.widgets import CKEditorWidget
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.html import format_html
from django.utils.html import mark_safe
import bulk_admin
from searchableselect.widgets import SearchableSelect


app = apps.get_app_config('vulgar')


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('page',)
        widgets = {
            'social_media_image': SearchableSelect(model='vulgar.Media', search_field='title', limit=10, many=False),
            'thumbnail_image': SearchableSelect(model='vulgar.Media', search_field='title', limit=10, many=False),
            'hero_image': SearchableSelect(model='vulgar.Media', search_field='title', limit=10, many=False),
        }
        # fields = '__all__'


class BlogAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = BlogAdminForm  


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogLanguage
        exclude = ('breadcrumb_title',)
        widgets = {
            'tags': SearchableSelect(model='vulgar.Tag', search_field='name', limit=10, many=True),
            'blog': SearchableSelect(model='vulgar.Blog', search_field='slug', limit=10, many=False),
        }
        # fields = '__all__'


class PostAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = PostAdminForm  


class CategoryLanguageAdminForm(forms.ModelForm):
    class Meta:
        model = CategoryLanguage
        fields = '__all__'


class CategoryLanguageAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = CategoryLanguageAdminForm  


models_except = [BlogLanguage, Media, CategoryLanguage, Tag, Blog]
for model_name, model in app.models.items():
    if not model in models_except:
        admin.site.register(model)

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogLanguage, PostAdmin)
admin.site.register(CategoryLanguage, CategoryLanguageAdmin)


# class MediaInline(bulk_admin.StackedBulkInlineModelAdmin):
#     model = Media
#     raw_id_fields = ['image_tag', 'title', 'alt_tag', 'media_type', 'photo', 'url']


@admin.register(Media)
class MediaAdmin(bulk_admin.BulkModelAdmin):
    fields = ['image_tag', 'title', 'alt_tag', 'media_type', 'photo', 'url']
    readonly_fields = ['image_tag']
    # bulk_inline = MediaInline

    def image_tag(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width='500px',
            height='300px',
            )
        )


@admin.register(Tag)
class TagAdmin(bulk_admin.BulkModelAdmin):
    fields = ['name', 'language', 'published_status']
    bulk_upload_fields = ()