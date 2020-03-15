from django.db import models
from enum import Enum
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishedStatusChoice(Enum): 
    DFT = 'Draft'
    ACT = 'Active'
    INACT = 'Inactive'


class Page(BaseModel):
    title = models.CharField(max_length=1000)
    published_status = models.CharField(max_length=100,
                                            choices=[(tag, tag.value) for tag in PublishedStatusChoice])
    published_date_from = models.DateTimeField()
    published_date_to = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=1000, default='')
    category_description = models.CharField(max_length=1000, default='')
    image = models.CharField(max_length=1000, default='')
    home_page_view = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(BaseModel):
    auth_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )


class Blog(BaseModel):
    title = models.CharField(max_length=1000)
    category = models.ManyToManyField(
        Category,
        related_name="blogs")
    slug = models.CharField(max_length=1000, default='')
    page = models.ForeignKey(Page, on_delete=models.PROTECT, blank=True, null=True)
    tags = models.ManyToManyField(
        Tag,
        related_name="blogs")
    hero_image = models.CharField(max_length=1000, default='')
    thumbnail_image = models.CharField(max_length=1000, default='')
    description = models.CharField(max_length=1000, default='')
    content = models.CharField(max_length=100000)
    published_status = models.CharField(max_length=100,
                                            choices=[(tag.value, tag.value) for tag in PublishedStatusChoice])
    published_date_from = models.DateTimeField()
    published_date_to = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
