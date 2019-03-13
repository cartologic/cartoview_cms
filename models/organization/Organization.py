from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class Organization(Page):
    template = 'cartoview_cms/organization/organization.html'
    parent_page_types = ['cartoview_cms.OrganizationsIndex']
    subpage_types = []
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', blank=True, null=True
    )
    link = models.URLField(max_length=120, blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('thumbnail'),
        FieldPanel('link'),
    ]
