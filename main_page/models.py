import uuid

from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField

from utils.generic import TimeStampMixin


class CompanySettings(TimeStampMixin):
    company_name = models.CharField('Company Name', max_length=50)
    email = models.EmailField('Email')
    logo = models.URLField('Company Logo URL')

    def __str__(self):
        return self.company_name


class SocialMedia(TimeStampMixin):
    social_media_id = models.UUIDField(
        'Social Media ID',
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
        editable=False)
    logo = models.URLField('URL Logo')
    unique_description = models.CharField(
        'Unique Description', max_length=50, unique=True)
    description = models.CharField('Description', max_length=50)
    company_settings = models.ForeignKey(
        CompanySettings, on_delete=models.CASCADE)
    url = models.URLField()
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.description


class HeaderContent(TimeStampMixin):
    title = models.CharField('Title', max_length=100)
    body = RichTextField()
    image = models.URLField()


class MainPageSectionContent(TimeStampMixin):
    title = models.CharField('Title', max_length=100)
    body = RichTextField()
    image = models.URLField()
    order = models.IntegerField('Display Order', unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']


class Subscription(TimeStampMixin):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    email = models.EmailField('Email', max_length=100)

    class Meta:
        ordering = ['create_date']