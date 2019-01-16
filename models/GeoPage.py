import json

from django.db import models
from django.dispatch import receiver
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from django.db.models.signals import pre_delete
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from geonode.maps.models import Map, MapLayer
from geonode.utils import resolve_object
from cartoview.app_manager.models import AppInstance, App

from .snippets.MapSnippet import MapSnippet


class GeoPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('email_field', blocks.EmailBlock()),
        ('integer', blocks.IntegerBlock()),
        ('float', blocks.FloatBlock()),
        ('decimal', blocks.DecimalBlock()),
        ('url', blocks.URLBlock()),
        ('check_box', blocks.BooleanBlock()),
        ('date', blocks.DateBlock()),
        ('time', blocks.TimeBlock()),
        ('date_time', blocks.DateTimeBlock()),
        ('paragraph', blocks.RichTextBlock()),
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
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
        SnippetChooserPanel('map'),
    ]

    def save(self, *args, **kwargs):
        app = App.objects.filter(name="cartoview_cms").first()
        if self.app_instance is None:
            app_instance = AppInstance(title=self.title, config=self.title, owner=self.owner, app=app)
            app_instance.save()
            self.app_instance = app_instance
        else:
            app_instance = self.app_instance
            app_instance.title = self.title
            app_instance.config = self.title
            app_instance.owner = self.owner
            app_instance.app = app
            app_instance.save()
        super(GeoPage, self).save()

    def get_context(self, request, *args, **kwargs):
        context = super(GeoPage, self).get_context(request)
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


@receiver(pre_delete, sender=GeoPage)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()
