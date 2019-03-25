from django import forms
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from ..countries.Country import Country


class Organization(Page):
    template = 'cartoview_cms/organization/organization.html'
    parent_page_types = ['cartoview_cms.OrganizationsIndex']
    subpage_types = []
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True
    )
    link = models.URLField(max_length=120, blank=True, null=True)
    related_country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="related_country", blank=True, null=True)
    main_organization = models.BooleanField(default=False, blank=False)
    organization_title = models.CharField(max_length=120, blank=True)
    organization_description = models.CharField(max_length=500, blank=True)


    content_panels = Page.content_panels + [
        ImageChooserPanel('thumbnail'),
        FieldPanel('link'),
        FieldPanel('related_country', widget=forms.Select),
        MultiFieldPanel([
            FieldPanel('main_organization'),
            FieldPanel('organization_title'),
            FieldPanel('organization_description'),
        ], heading="Main Organization Section"),
    ]
