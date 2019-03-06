from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from .blocks.fields import BodyStreamBlock


class StaticPage(Page):
    body = StreamField(BodyStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
