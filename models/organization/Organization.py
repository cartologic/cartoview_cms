from django.db import models
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class Organization(Page):
    template = 'cartoview_cms/organization/organization.html'
    parent_page_types = ['cartoview_cms.OrganizationsIndex']
    subpage_types = []
    main_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', blank=True, null=True
    )
    intro = models.CharField(max_length=500, blank=True, null=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('HTML', blocks.RawHTMLBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('page_chooser', blocks.PageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        StreamFieldPanel("body", classname="Full"),
    ]
