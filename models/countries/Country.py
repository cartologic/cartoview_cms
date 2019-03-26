from django import forms
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from geonode.documents.models import Document
from geonode.maps.models import Map
from ..case_study.CaseStudy import CaseStudy
from ..news.NewsItem import NewsItem
from ..streamfields.Blocks import ImageTextOverlayBlock, AccordionBlock, HeaderBlock, TabBlock, TextFieldBlock, \
    UnorderedListBlock, ImageGalleryBlock
from ..streamfields.MapBlock import MapBlock

class Country(Page):
    template = 'cartoview_cms/countries/country.html'
    parent_page_types = ['cartoview_cms.CountriesIndex']
    subpage_types = []
    abstract = models.CharField(max_length=120, blank=True, null=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
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
        ('map', blocks.ListBlock(
            MapBlock(),
            template='cartoview_cms/streamfields/map.html',
            icon='fa-globe', ))
        ,
    ], blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("abstract", classname="full"),
        ImageChooserPanel('main_image'),
        StreamFieldPanel("body", classname="Full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    def get_context(self, request):
        context = super(Country, self).get_context(request)
        case_studies = CaseStudy.objects.filter(categories__in=self.categories.all())
        news_items = NewsItem.objects.filter(categories__in=self.categories.all())
        maps = Map.objects.filter(category__identifier__in=self.categories.all().values('name'))
        documents = Document.objects.filter(category__identifier__in=self.categories.all().values('name'))
        context['case_studies'] = case_studies
        context['news_items'] = news_items
        context['maps'] = maps
        context['documents'] = documents
        return context
