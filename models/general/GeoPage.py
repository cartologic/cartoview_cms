import json

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from geonode.maps.models import Map
from geonode.documents.models import Document
from cartoview.app_manager.models import App, AppInstance
from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from ..case_study.CaseStudy import CaseStudy
from ..news.NewsItem import NewsItem
from ..countries.Country import Country
from geonode.base.models import TopicCategory
from .ContentCategory import ContentCategory
from ..streamfields.Blocks import ImageTextOverlayBlock, AccordionBlock, HeaderBlock, TabBlock, TextFieldBlock, \
    UnorderedListBlock, ImageGalleryBlock


class GeoPage(Page):
    template = 'cartoview_cms/general/geo_page.html'
    parent_page_types = ['cartoview_cms.ContentGroup', 'cartoview_cms.MenuItem']
    subpage_types = []
    show_in_menus_default = True
    abstract = models.CharField(max_length=120, blank=True, null=True)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', blank=True, null=True
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('document', DocumentChooserBlock()),
        ('header', blocks.ListBlock(
            HeaderBlock(),
            template='cartoview_cms/streamfields/header.html',
            icon="title", ))
        ,
        ('text_field', blocks.ListBlock(
            TextFieldBlock(),
            template='cartoview_cms/streamfields/text_field.html',
            icon="fa-text-width", ))
        ,
        ('list', blocks.ListBlock(
            UnorderedListBlock(),
            template='cartoview_cms/streamfields/list.html',
            icon="list-ul"))
        ,
        ('accordions', blocks.ListBlock(
            AccordionBlock(),
            template='cartoview_cms/streamfields/accordion.html',
            icon='list-ol', ))
        ,
        ('horizontal_tabs', blocks.ListBlock(
            TabBlock(),
            template='cartoview_cms/streamfields/horizontal_tab.html',
            icon='list-ol', ))
        ,
        ('verticale_tabs', blocks.ListBlock(
            TabBlock(),
            template='cartoview_cms/streamfields/vertical_tab.html',
            icon='list-ol', ))
        ,
        ('image_text_overlay', blocks.ListBlock(
            ImageTextOverlayBlock(),
            template='cartoview_cms/streamfields/image_text_overlay.html',
            icon='fa-image', ))
        ,
        ('image_gallery', blocks.ListBlock(
            ImageGalleryBlock(),
            template='cartoview_cms/streamfields/image_gallery.html',
            icon='fa-camera-retro', ))
        ,
    ], blank=True)
    content_category = models.ForeignKey('cartoview_cms.ContentCategory', on_delete=models.PROTECT)
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content_category', widget=forms.Select),
        FieldPanel("abstract", classname="full"),
        ImageChooserPanel('thumbnail'),
        StreamFieldPanel("body", classname="Full"),
    ]

    def get_context(self, request):
        context = super(GeoPage, self).get_context(request)
        case_studies = CaseStudy.objects.filter(categories=self.content_category)
        news_items = NewsItem.objects.filter(categories=self.content_category)
        maps = Map.objects.filter(category=self.category)
        documents = Document.objects.filter(category=self.category)
        countries = Country.objects.filter(categories=self.content_category)
        context['case_studies'] = case_studies
        context['news_items'] = news_items
        context['maps'] = maps
        context['documents'] = documents
        context['countries'] = countries
        return context

    def save(self, *args, **kwargs):
        app = App.objects.filter(name="cartoview_cms").first()
        ContentCategory.assure_category_exists(self.content_category.name)
        category = TopicCategory.objects.filter(identifier=self.content_category.name).first()
        self.category = category
        if self.app_instance is None:
            app_instance = AppInstance(
                title=self.title,
                config=json.dumps({
                    'title': self.title,
                    'abstract': self.abstract
                }),
                owner=self.owner,
                app=app,
                abstract=self.abstract,
                category=category
            )
            app_instance.save()
            self.app_instance = app_instance
        else:
            app_instance = self.app_instance
            app_instance.title = self.title
            app_instance.config = json.dumps({
                'title': self.title,
                'abstract': self.abstract
            })
            app_instance.owner = self.owner
            app_instance.app = app
            app_instance.abstract = self.abstract
            app_instance.category = category
            app_instance.save()
        super(GeoPage, self).save()
