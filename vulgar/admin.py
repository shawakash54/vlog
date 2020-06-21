from django.contrib import admin
from django.apps import apps
from django import forms
from vulgar.models import BlogLanguage, Media, CategoryLanguage
from ckeditor.widgets import CKEditorWidget
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.html import format_html
from django.utils.html import mark_safe

app = apps.get_app_config('vulgar')

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogLanguage
        fields = '__all__'


class PostAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = PostAdminForm  


class CategoryLanguageAdminForm(forms.ModelForm):
    class Meta:
        model = CategoryLanguage
        fields = '__all__'


class CategoryLanguageAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = CategoryLanguageAdminForm  


models_except = [BlogLanguage, Media, CategoryLanguage]
for model_name, model in app.models.items():
    if not model in models_except:
        admin.site.register(model)

admin.site.register(BlogLanguage, PostAdmin)
admin.site.register(CategoryLanguage, CategoryLanguageAdmin)



@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    fields = ['image_tag', 'title', 'alt_tag', 'media_type', 'photo', 'url']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width='500px',
            height='300px',
            )
        )
