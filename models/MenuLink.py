from django.db import models
from django.shortcuts import redirect
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page


class MenuLink(Page):
    link_external = models.URLField("External link", blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('link_external'),
    ]

    def serve(self, request, *args, **kwargs):
        return redirect(self.link_external, permanent=False)
