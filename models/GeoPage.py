from cartoview.app_manager.models import App
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


class GeoPage(Page):
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
    category = models.ForeignKey('cartoview_cms.ContentCategory', on_delete=models.PROTECT)

    content_panels = Page.content_panels + [
        FieldPanel('category', widget=forms.Select),
        FieldPanel("abstract", classname="full"),
        StreamFieldPanel("body", classname="Full"),
    ]

    def save(self, *args, **kwargs):
        app = App.objects.filter(name="cartoview_cms").first()
        category = TopicCategory.objects.filter(identifier=self.category_identifier).first()
        thumbnail_url = ""
        self.category = category
        if self.map is not None:
            thumbnail_url = self.map.map_object.thumbnail_url
        if self.app_instance is None:
            app_instance = AppInstance(
                title=self.title,
                config=json.dumps({
                    'title': self.title,
                    'abstract': self.abstract
                }),
                owner=self.owner,
                app=app,
                thumbnail_url=thumbnail_url,
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
            app_instance.thumbnail_url = thumbnail_url
            app_instance.abstract = self.abstract
            app_instance.category = category
            app_instance.save()
        super(CoastalCliffInstability, self).save()

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
