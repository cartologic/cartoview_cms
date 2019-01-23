import json

from django.db import models
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from geonode.base.models import TopicCategory
from geonode.maps.models import Map, MapLayer
from geonode.utils import resolve_object

from .snippets.MapSnippet import MapSnippet


class BaseGeoPage(Page):
    is_creatable = False
    abstract = models.CharField(max_length=120, blank=True, null=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('email_field', blocks.EmailBlock()),
        ('integer', blocks.IntegerBlock()),
        ('float', blocks.FloatBlock()),
        ('decimal', blocks.DecimalBlock()),
        ('url', blocks.URLBlock()),
        ('check_box', blocks.BooleanBlock()),
        ('date', blocks.DateBlock()),
        ('time', blocks.TimeBlock()),
        ('date_time', blocks.DateTimeBlock()),
        ('HTML', blocks.RawHTMLBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('choice', blocks.ChoiceBlock()),
        ('page_chooser', blocks.PageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], blank=True)
    map = models.ForeignKey(
        MapSnippet,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("abstract", classname="full"),
        StreamFieldPanel("body", classname="Full"),
        SnippetChooserPanel('map'),
    ]

    @staticmethod
    def assure_category_exists(identifier, description, gn_description):
        num_results = TopicCategory.objects.filter(identifier=identifier).count()
        if num_results == 0:
            temp_category = TopicCategory(
                identifier=identifier,
                description=description,
                gn_description=gn_description
            )
            temp_category.save()

    def get_context(self, request, *args, **kwargs):
        context = super(BaseGeoPage, self).get_context(request)
        if self.map is not None:
            id = self.map.map_object.id
            key = 'pk'
            map_obj = resolve_object(
                request, Map, {key: id},
                permission='base.change_resourcebase',
                permission_msg='You do not have permissions for this map.', **kwargs)
            config = map_obj.viewer_json(request)
            config = json.dumps(config)
            layers = MapLayer.objects.filter(map=map_obj.id)
            links = map_obj.link_set.download()
            group = None

            context['config'] = config
            context['resource'] = map_obj
            context['group'] = group
            context['layers'] = layers
            context['links'] = links
        return context
