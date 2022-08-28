from django.db import models


class TimeStampMixin(models.Model):
    create_date = models.DateTimeField(
        ('Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(
        ('Update Date'), auto_now=True)

    class Meta:
        abstract = True
