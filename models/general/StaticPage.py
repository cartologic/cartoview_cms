from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from ..streamfields.Blocks import ImageTextOverlayBlock, AccordionBlock, HeaderBlock, TabBlock, TextFieldBlock, \
    UnorderedListBlock, ImageGalleryBlock
from ..streamfields.MapBlock import MapBlock


class StaticPage(Page):
    template = 'cartoview_cms/general/static_page.html'
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(classname="full")),
        ('document', DocumentChooserBlock()),
        ('header', blocks.ListBlock(
            HeaderBlock(),
            template='cartoview_cms/streamfields/header.html',
            icon="title", ))
        ,
        ('text_field', blocks.ListBlock(
            TextFieldBlock(),
            template='cartoview_cms/streamfields/text_field.html',
            icon="fa-text-width", ))
        ,
        ('list', blocks.ListBlock(
            UnorderedListBlock(),
            template='cartoview_cms/streamfields/list.html',
            icon="list-ul"))
        ,
        ('accordions', blocks.ListBlock(
            AccordionBlock(),
            template='cartoview_cms/streamfields/accordion.html',
            icon='list-ol', ))
        ,
        ('horizontal_tabs', blocks.ListBlock(
            TabBlock(),
            template='cartoview_cms/streamfields/horizontal_tab.html',
            icon='list-ol', ))
        ,
        ('verticale_tabs', blocks.ListBlock(
            TabBlock(),
            template='cartoview_cms/streamfields/vertical_tab.html',
            icon='list-ol', ))
        ,
        ('image_text_overlay', blocks.ListBlock(
            ImageTextOverlayBlock(),
            template='cartoview_cms/streamfields/image_text_overlay.html',
            icon='fa-image', ))
        ,
        ('image_gallery', blocks.ListBlock(
            ImageGalleryBlock(),
            template='cartoview_cms/streamfields/image_gallery.html',
            icon='fa-camera-retro', ))
        ,
        ('map', blocks.ListBlock(
            MapBlock(),
            template='cartoview_cms/streamfields/map.html',
            icon='fa-globe', ))
        ,
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]
