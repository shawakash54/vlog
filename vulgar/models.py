from django.db import models
from enum import Enum
from django.conf import settings
from cities_light.models import City, Country
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify
from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models
import os
from uuid import uuid4

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    updated_at = models.DateTimeField(auto_now=True, db_index=True,)

    class Meta:
        abstract = True


class PublishedStatusChoice(Enum): 
    DFT = 'Draft'
    ACT = 'Active'
    INACT = 'Inactive'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_status='Active')


def getParentPublishedManager(*args, **kwargs):
    class ParentPublishedManager(models.Manager):
        def get_queryset(self): 
            return super().get_queryset().filter(*args, **kwargs)
        
    return ParentPublishedManager()

class Language(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    code = models.CharField(max_length=20, db_index=True, default='')
    country = models.ManyToManyField(Country)
    slug = models.CharField(max_length=100, db_index=True)
    is_default = models.BooleanField(default=False)

    published_status = models.CharField(max_length=100,
                                            choices=[(tag.value, tag.value) for tag in PublishedStatusChoice],
                                            default='Active')
    objects = models.Manager()
    published_objects = PublishedManager() 
    display_name = models.CharField(max_length=1000, db_index=True, default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.code)
        super(Language, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Page(BaseModel):
    title = models.CharField(max_length=1000, db_index=True)
    published_status = models.CharField(max_length=100,
                                            choices=[(tag.value, tag.value) for tag in PublishedStatusChoice],
                                            default='Active')
    published_date_from = models.DateTimeField()
    published_date_to = models.DateTimeField()

    def __str__(self):
        return self.title


class MediaTypeChoice(Enum): 
    doc = 'document'
    img = 'image'
    vid = 'video'


class MediaType(BaseModel):
    media_type = models.CharField(max_length=100, db_index=True,
                                    choices=[(media_type.value, media_type.value) for media_type in MediaTypeChoice])
    def __str__(self):
        return self.media_type


class Media(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    photo = models.FileField()
    alt_tag = models.CharField(max_length=100, db_index=True)
    media_type = models.ForeignKey(MediaType, on_delete=models.PROTECT)
    url = models.CharField(max_length=1000, default='', blank=True, null=True, db_index=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        file_extension = os.path.splitext(self.photo.name)[1]
        self.photo.name = slugify(self.title) + file_extension
        self.url = self.photo.url
        super(Media, self).save(*args, **kwargs)


class Category(BaseModel):
    slug = models.CharField(max_length=1000, default='', db_index=True)
    image = models.ForeignKey(Media, on_delete=models.PROTECT, blank=True, null=True)
    social_media_image = models.ForeignKey(Media, on_delete=models.PROTECT, 
                                                related_name='categories_social_media', 
                                                blank=True, 
                                                null=True,
                                                help_text="Minimum dimension - 1200×630 pixels, aspect ratio - 1.91:1, Size < 1MB")
    home_page_view = models.BooleanField(default=False)
    published_status = models.CharField(max_length=100,
                                            choices=[(tag.value, tag.value) for tag in PublishedStatusChoice],
                                            default='Active')
    objects = models.Manager()
    published_objects = PublishedManager()                                          
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs) 


    def __str__(self):
        return self.slug


class CategoryLanguage(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=100)
    breadcrumb_title = models.CharField(max_length=20, default='')
    meta_keywords = ArrayField(
                        models.CharField(max_length=50),
                        default=list
                    )
    meta_description = models.CharField(max_length=1000, default='')
    category_description = models.CharField(max_length=1000, default='')
    objects = models.Manager()
    published_objects = getParentPublishedManager(category__published_status='Active')

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, blank=True, null=True)
    published_status = models.CharField(max_length=100,
                                            choices=[(tag.value, tag.value) for tag in PublishedStatusChoice],
                                            default='Active')
    objects = models.Manager()
    published_objects = PublishedManager()  

    def __str__(self):
        return self.name


# class TagLanguage(BaseModel):
#     name = models.CharField(max_length=100, db_index=True)
#     language = models.ForeignKey(
#         Language, on_delete=models.PROTECT, blank=True, null=True)
    
#     def __str__(self):
#         return self.name



class User(BaseModel):
    auth_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    bio = models.CharField(max_length=1000, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.auth_user.first_name


class Blog(BaseModel):
    category = models.ManyToManyField(
        Category,
        related_name="blogs")
    primary_category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    slug = models.CharField(max_length=1000, default='', db_index=True)
    page = models.ForeignKey(Page, on_delete=models.PROTECT, blank=True, null=True)
    hero_image = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='blogs_hero', blank=True, null=True)
    thumbnail_image = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='blogs_thumbnail', blank=True, null=True)
    social_media_image = models.ForeignKey(Media, on_delete=models.PROTECT, 
                                                related_name='blogs_social_media', 
                                                blank=True, 
                                                null=True,
                                                help_text="Minimum dimension - 1200×630 pixels, aspect ratio - 1.91:1, Size < 1MB")
    published_status = models.CharField(max_length=100,
                                            choices=[(tag.value, tag.value) for tag in PublishedStatusChoice],
                                            default='Active')

    objects = models.Manager()
    published_objects = PublishedManager()  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs) 

    def __str__(self):
        return self.slug

class BlogLanguage(BaseModel):
    blog = models.ForeignKey(
        Blog, on_delete=models.PROTECT, blank=True, null=True)
    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=1000, db_index=True)
    breadcrumb_title = models.CharField(max_length=20, default='')
    meta_keywords = ArrayField(
                        models.CharField(max_length=50),
                        default=list
                    )
    tags = models.ManyToManyField(
        Tag,
        related_name="blogs")
    meta_description = models.CharField(max_length=1000, default='')
    description = models.CharField(max_length=1000, default='')
    content = models.CharField(max_length=100000)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    objects = models.Manager()
    published_objects = getParentPublishedManager(blog__published_status='Active')

    def __str__(self):
        return self.title



class Feedback(BaseModel):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    email_id = models.CharField(max_length=100, db_index=True)
    contact_number = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    subject = models.CharField(max_length=1000, blank=True, null=True)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.first_name + '--' + self.email_id


class NewsLetterSubscription(BaseModel):
    email_id = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.email_id


class FailedUserQuery(BaseModel):
    search_query = models.CharField(max_length=1000, db_index=True)
    search_count = models.IntegerField(default=0, db_index=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)

    def __str__(self):
        return self.search_query

