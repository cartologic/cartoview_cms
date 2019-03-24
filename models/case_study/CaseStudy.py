from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from ..streamfields.Blocks import ImageTextOverlayBlock, AccordionBlock, HeaderBlock, TabBlock, TextFieldBlock, \
    UnorderedListBlock, ImageGalleryBlock

from geonode import settings


class CaseStudy(Page):
    template = 'cartoview_cms/case_study/case_study.html'
    parent_page_types = ['cartoview_cms.CaseStudyIndex']
    subpage_types = []
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
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='authors', blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel("abstract", classname="full"),
        ImageChooserPanel('thumbnail'),
        StreamFieldPanel("body", classname="Full"),
    ]
