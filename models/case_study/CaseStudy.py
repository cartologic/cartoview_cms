from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, InlinePanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

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
        ('HTML', blocks.RawHTMLBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('page_chooser', blocks.PageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], blank=True)
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='authors', blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel("abstract", classname="full"),
        ImageChooserPanel('thumbnail'),
        StreamFieldPanel("body", classname="Full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
