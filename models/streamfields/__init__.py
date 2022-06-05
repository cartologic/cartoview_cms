"""
Customize CodeRed original LAYOUT_STREAMBLOCKS
to include previously created streamfield blocks
"""
from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks
from coderedcms.blocks import (
    ButtonBlock,
    CardBlock,
    CardGridBlock,
    CarouselBlock,
    DownloadBlock,
    EmbedGoogleMapBlock,
    EmbedVideoBlock,
    GridBlock,
    HeroBlock,
    ImageBlock,
    ImageGalleryBlock,
    ImageLinkBlock,
    ModalBlock,
    PageListBlock,
    PagePreviewBlock,
    PriceListBlock,
    QuoteBlock,
    ReusableContentBlock,
    RichTextBlock,
    TableBlock,
)
from .Blocks import (
    AccordionBlock,
    HeaderBlock,
    ImageTextOverlayBlock,
    MapBlock,
    MapCatalogBlock,
    UnorderedListBlock
)


CUSTOM_HTML_STREAMBLOCKS = [
    ('header', HeaderBlock()),
    ('text', RichTextBlock(icon='fa-file-text-o')),
    ('button', ButtonBlock()),
    ('image', ImageBlock()),
    ('image_text_overlay', ImageTextOverlayBlock()),
    ('image_link', ImageLinkBlock()),
    ('list', UnorderedListBlock()),
    ('html', blocks.RawHTMLBlock(icon='code', form_classname='monospace', label=_('HTML'), )),
    ('accordions', AccordionBlock()),
    ('download', DownloadBlock()),
    ('embed_video', EmbedVideoBlock()),
    ('quote', QuoteBlock()),
    ('table', TableBlock()),
    ('google_map', EmbedGoogleMapBlock()),
    ('page_list', PageListBlock()),
    ('page_preview', PagePreviewBlock()),
]

# TODO: Include CodeRed ImageGalleryBlock here when GeoNode upgrades to bootstrap 4.
CUSTOM_CONTENT_STREAMBLOCKS = CUSTOM_HTML_STREAMBLOCKS + [
    ('card', CardBlock()),
    ('carousel', CarouselBlock()),
    ('modal', ModalBlock(CUSTOM_HTML_STREAMBLOCKS)),
    ('map', MapBlock()),
    ('map_catalog', MapCatalogBlock()),
    ('pricelist', PriceListBlock()),
    ('reusable_content', ReusableContentBlock()),
]

CUSTOM_LAYOUT_STREAMBLOCKS = [
    ('hero', HeroBlock([
        ('row', GridBlock(CUSTOM_CONTENT_STREAMBLOCKS)),
        ('cardgrid', CardGridBlock([('card', CardBlock()), ])),
        ('html', blocks.RawHTMLBlock(icon='code', form_classname='monospace', label=_('HTML'))),
    ])),
    ('row', GridBlock(CUSTOM_CONTENT_STREAMBLOCKS)),
    ('cardgrid', CardGridBlock([('card', CardBlock()), ])),
    ('html', blocks.RawHTMLBlock(icon='code', form_classname='monospace', label=_('HTML'))),
]
