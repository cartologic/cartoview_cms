import json

from cartoview.app_manager.models import App, AppInstance
from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from geonode.base.models import TopicCategory
from .ContentCategory import ContentCategory


class GeoPage(Page):
    template = 'cartoview_cms/general/geo_page.html'
    parent_page_types = ['cartoview_cms.ContentGroup']
    subpage_types = []
    show_in_menus_default = True
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
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("abstract", classname="full"),
        StreamFieldPanel("body", classname="Full"),
    ]

    def save(self, *args, **kwargs):
        app = App.objects.filter(name="cartoview_cms").first()
        ContentCategory.assure_category_exists(self.get_parent().contentgroup.content_category.name)
        category = TopicCategory.objects.filter(identifier=self.get_parent().contentgroup.content_category.name).first()
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
