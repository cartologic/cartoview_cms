from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class ContentCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Content Categories'
