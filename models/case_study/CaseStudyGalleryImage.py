from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .CaseStudy import CaseStudy


class CaseStudyGalleryImage(Orderable):
    page = ParentalKey(CaseStudy, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
