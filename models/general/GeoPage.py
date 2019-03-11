import json

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

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

from ..case_study.CaseStudy import CaseStudy
from geonode.base.models import TopicCategory
from .ContentCategory import ContentCategory


class GeoPage(Page):
    template = 'cartoview_cms/general/geo_page.html'
    parent_page_types = ['cartoview_cms.ContentGroup', 'cartoview_cms.MenuItem']
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
    content_category = models.ForeignKey('cartoview_cms.ContentCategory', on_delete=models.PROTECT)
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)

    def gallery_image_count(self):
        return self.gallery_images.count()
    def gallery_image_controller_count(self):
        return self.gallery_images.count()/4

    content_panels = Page.content_panels + [
        FieldPanel('content_category', widget=forms.Select),
        FieldPanel("abstract", classname="full"),
        StreamFieldPanel("body", classname="Full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def get_context(self, request):
        context = super(GeoPage, self).get_context(request)
        # Filter by category title
        case_studies = CaseStudy.objects.filter(categories=self.content_category)
        context['case_studies'] = case_studies
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
