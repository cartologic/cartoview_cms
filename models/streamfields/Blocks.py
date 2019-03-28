from django import forms
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from geonode.maps.models import Map


class MapChooserBlock(blocks.ChooserBlock):
    target_model = Map
    widget = forms.Select

    class Meta:
        icon = "icon"

    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class MapBlock(blocks.StructBlock):
    map = MapChooserBlock(required=True)

    class Meta:
        template = 'cartoview_cms/streamfields/map.html'
        icon = 'fa-globe'


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label='Title',
        max_length=50,
    )
    content = blocks.RichTextBlock(
        label='Content',
    )

    class Meta:
        template = 'cartoview_cms/streamfields/accordion.html'
        icon = 'list-ol'


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

    class Meta:
        template = 'cartoview_cms/streamfields/header.html'
        icon = "title"


class ImageGalleryBlock(blocks.StructBlock):
    image = blocks.ListBlock(
        ImageChooserBlock(),
        icon='image',
        label='Image',
    )

    class Meta:
        template = 'cartoview_cms/streamfields/image_gallery.html'
        icon = 'fa-camera-retro'


class ImageTextOverlayBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=200,
    )

    class Meta:
        template = 'cartoview_cms/streamfields/image_text_overlay.html'
        icon = 'fa-image'


class SeparatorBlock(blocks.StaticBlock):
    class Meta:
        icon = 'fa-window-minimize'
        admin_text = mark_safe('<b>Separator</b>: no configuration needed.')
        template = 'cartoview_cms/streamfields/separator.html'


class UnorderedListBlock(blocks.StructBlock):
    content = blocks.ListBlock(
        blocks.CharBlock(),
        label='Items',
    )

    class Meta:
        template = 'cartoview_cms/streamfields/list.html'
        icon = "list-ul"


class UserChooserBlock(blocks.ChooserBlock):
    target_model = get_user_model()
    widget = forms.Select

    class Meta:
        icon = "icon"

    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class RelatedUsersBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label='Title',
        max_length=200,
        help_text="Section title as it appears to the users"
    )
    users = blocks.ListBlock(UserChooserBlock(required=True), label='Users')

    class Meta:
        template = 'cartoview_cms/streamfields/related_users.html'
        icon = "fa-users"


class DisplaySizeChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('1', '1 - Smallest'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4 - Recommended'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12 - Largest'),
    )


class RelatedPages(blocks.StructBlock):
    title = blocks.CharBlock(
        label='Title',
        max_length=200,
        help_text="Section title as it appears to the users"
    )
    display_size = DisplaySizeChoiceBlock(
        label='Display Size',
        default='4',
    )
    pages = blocks.ListBlock(
        blocks.PageChooserBlock(target_model='cartoview_cms.GenericPage'),
        label='Items',
    )

    class Meta:
        template = 'cartoview_cms/streamfields/related_module.html'
        icon = 'fa-window-restore'
