from django.contrib import admin
from django.apps import apps
from django import forms
from vulgar.models import BlogLanguage
from ckeditor.widgets import CKEditorWidget
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

app = apps.get_app_config('vulgar')

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogLanguage
        fields = '__all__'


class PostAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = PostAdminForm  

for model_name, model in app.models.items():
    if not model is BlogLanguage:
        admin.site.register(model)

admin.site.register(BlogLanguage, PostAdmin)
