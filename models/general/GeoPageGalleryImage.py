from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .GeoPage import GeoPage


class GeoPageGalleryImage(Orderable):
    page = ParentalKey(GeoPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
