from django.contrib import admin
from django.apps import apps
from django import forms
from vulgar.models import Blog
from ckeditor.widgets import CKEditorWidget

app = apps.get_app_config('vulgar')

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm  

for model_name, model in app.models.items():
    if not model is Blog:
        admin.site.register(model)

admin.site.register(Blog, PostAdmin)
