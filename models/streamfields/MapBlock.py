from django import forms
from wagtail.wagtailcore import blocks

from geonode.maps.models import Map


class MapChooserBlock(blocks.ChooserBlock):
    target_model = Map
    widget = forms.Select

    class Meta:
        icon = "icon"

    # Return the key value for the select field
    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value



class MapBlock(blocks.StructBlock):
    map = MapChooserBlock(required=True)

