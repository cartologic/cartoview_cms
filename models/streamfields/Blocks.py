from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from .IconChooserBlock import IconChooserBlock


class GridChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('col-sm-12', '12'),
        ('col-sm-11', '11'),
        ('col-sm-10', '10'),
        ('col-sm-9', '9'),
        ('col-sm-8', '8'),
        ('col-sm-7', '7'),
        ('col-sm-6', '6'),
        ('col-sm-5', '5'),
        ('col-sm-4', '4'),
        ('col-sm-3', '3'),
        ('col-sm-2', '2'),
        ('col-sm-1', '1'),
    ]


class HeaderChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6'),
    )


class HeaderBlock(blocks.StructBlock):
    header = HeaderChoiceBlock(
        label='Header Size',
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=50,
    )


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label='Title',
        max_length=50,
    )
    content = blocks.RichTextBlock(
        label='Content',
    )


class TabBlock(blocks.StructBlock):
    icon = IconChooserBlock(
        label='Icon',
        required=False,
    )
    title = blocks.CharBlock(
        label='Title',
        max_length=50,
    )
    content = blocks.RichTextBlock(
        label='Content',
    )


class ImageTextOverlayBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=200,
    )


class TextFieldBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(
        label='Text Field',
    )


class UnorderedListBlock(blocks.StructBlock):
    content = blocks.ListBlock(
        blocks.CharBlock(),
        label='Items',
    )


class ImageGalleryBlock(blocks.StructBlock):
    image = blocks.ListBlock(
        ImageChooserBlock(),
        icon='image',
        label='Image',
    )
