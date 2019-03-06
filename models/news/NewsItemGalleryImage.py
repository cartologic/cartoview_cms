from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .NewsItem import NewsItem


class NewsItemGalleryImage(Orderable):
    page = ParentalKey(NewsItem, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
