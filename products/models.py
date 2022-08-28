import uuid
from django.db import models
from ckeditor.fields import RichTextField

from utils.generic import TimeStampMixin


class Product(TimeStampMixin):
    product_id = models.UUIDField(
        'Product ID',
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
        editable=False)
    title = models.CharField('Title', max_length=100)
    summary = models.CharField('Summary', max_length=300)
    body = RichTextField()
    image = models.ImageField(upload_to='products')
    order = models.IntegerField('Display Order', unique=True)
    more_popular = models.BooleanField('More Popular', default=False)
    url = models.URLField('Amazon URL')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title