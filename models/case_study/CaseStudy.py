import json

from modelcluster.fields import ParentalManyToManyField

from cartoview.app_manager.models import App, AppInstance
from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, InlinePanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from geonode.base.models import TopicCategory
from ..general.ContentCategory import ContentCategory


class CaseStudy(Page):
    template = 'cartoview_cms/case_study/case_study.html'
    parent_page_types = ['cartoview_cms.CaseStudyIndex']
    subpage_types = []
    show_in_menus_default = True
    abstract = models.CharField(max_length=120, blank=True, null=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('HTML', blocks.RawHTMLBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('page_chooser', blocks.PageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], blank=True)
    categories = ParentalManyToManyField('cartoview_cms.ContentCategory', blank=True)
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)

    def gallery_image_count(self):
        return self.gallery_images.count()
    def gallery_image_controller_count(self):
        return self.gallery_images.count()/4

    content_panels = Page.content_panels + [
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel("abstract", classname="full"),
        StreamFieldPanel("body", classname="Full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
