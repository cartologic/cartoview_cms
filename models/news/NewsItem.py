from django import forms
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailcore import blocks

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .NewsItemTag import NewsItemTag
from ..streamfields.Blocks import ImageTextOverlayBlock, AccordionBlock, HeaderBlock, TabBlock, TextFieldBlock, \
    UnorderedListBlock, ImageGalleryBlock
from ..streamfields.MapBlock import MapBlock


class NewsItem(Page):
    template = 'cartoview_cms/news/news_item.html'
    parent_page_types = ['cartoview_cms.NewsIndex', 'cartoview_cms.NewsItem']
    subpage_types = ['cartoview_cms.NewsItem']
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    thumbnail = models.ForeignKey(
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
    tags = ClusterTaggableManager(through=NewsItemTag, blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="News information"),
        FieldPanel('intro'),
        ImageChooserPanel('thumbnail'),
        StreamFieldPanel("body", classname="Full"),
    ]
