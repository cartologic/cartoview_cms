import json
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from django.db import models
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel, PageChooserPanel, \
    FieldRowPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from cartoview.app_manager.models import AppInstance, App
from ..streamfields.Blocks import *


class GenericPage(Page):
    parent_page_types = ['wagtailcore.Page', 'cartoview_cms.GenericModule', 'cartoview_cms.GenericPage',
                         'cartoview_cms.MenuItem']
    subpage_types = ['cartoview_cms.GenericPage']
    show_in_menus_default = False

    selected_template = models.CharField(max_length=255, choices=(
        ('cartoview_cms/generic_module/generic_page_default.html', 'Default Template'),
    ), default='cartoview_cms/generic_module/generic_page_default.html')
    abstract = models.CharField(max_length=500, blank=True, null=True)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, blank=True, null=True
    )
    focused = models.BooleanField(default=False, verbose_name="Focused", help_text=mark_safe(
        "You should select the <b>focused template</b> for the Generic Module!."))
    related_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+',
                                     on_delete=models.SET_NULL)
    is_redirect = models.BooleanField(default=False, verbose_name="Redirect External",
                                      help_text=mark_safe("Redirct to an <b>External</b> link"))
    redirect_link = models.CharField(max_length=500, blank=True, null=True)
    body = StreamField([
        ('header', HeaderBlock()),
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('document', DocumentChooserBlock()),
        ('list', UnorderedListBlock()),
        ('accordions', AccordionBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('image_gallery', ImageGalleryBlock()),
        ('map', MapBlock()),
        ('separator', SeparatorBlock()),
        ('related_users', RelatedUsersBlock()),
        ('related_module', RelatedPages())
    ], blank=True)
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def template(self):
        return self.selected_template

    content_panels = Page.content_panels + [
        FieldPanel("abstract", classname="full"),
        MultiFieldPanel([
            FieldPanel('selected_template', widget=forms.Select),
            ImageChooserPanel('thumbnail'),
            FieldPanel('focused', widget=forms.CheckboxInput),
            PageChooserPanel('related_page'),
            FieldRowPanel([
                FieldPanel('is_redirect', classname="col4"),
                FieldPanel('redirect_link', classname="col8"),
            ]),
        ], heading="Display Information"),
        StreamFieldPanel("body", classname="Full"),
    ]

    def save(self, *args, **kwargs):
        app = App.objects.filter(name="cartoview_cms").first()
        thumbnail_url = None
        if self.thumbnail:
            thumbnail_url = self.thumbnail.file.url
        if self.app_instance is None:
            app_instance = AppInstance(
                title=self.title,
                config=json.dumps({
                    'title': self.title,
                    'abstract': self.abstract,
                    'url': self.url,
                    'id': self.id
                }),
                owner=self.owner,
                app=app,
                abstract=self.abstract,
                thumbnail_url=thumbnail_url
            )
            app_instance.save()
            self.app_instance = app_instance
        else:
            app_instance = self.app_instance
            app_instance.title = self.title
            app_instance.config = json.dumps({
                'title': self.title,
                'abstract': self.abstract,
                'url': self.url,
                'id': self.id
            })
            app_instance.owner = self.owner
            app_instance.app = app
            app_instance.abstract = self.abstract
            app_instance.thumbnail_url = thumbnail_url
            app_instance.save()
        super(GenericPage, self).save()
