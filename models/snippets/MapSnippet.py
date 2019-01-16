from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet

from geonode.maps.models import Map


@register_snippet
class MapSnippet(models.Model):
    map_title = models.CharField(max_length=120, null=True, blank=True)
    map_object = models.ForeignKey(Map)

    panels = [
        FieldPanel('map_title'),
        FieldPanel('map_object'),
    ]

    def __str__(self):
        return self.map_title
