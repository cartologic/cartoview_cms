# Generated by Django 2.2.12 on 2020-11-15 20:58

import cartoview_cms.models.streamfields.Blocks
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='clean_name',
            field=models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type'),
        ),
        migrations.AlterField(
            model_name='genericmodule',
            name='first_title',
            field=models.CharField(blank=True, help_text='You should select the <b>focused template</b> for this to work!', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='genericmodule',
            name='public_display',
            field=models.BooleanField(default=False, help_text="If checked, this module's children will be visible in <b>frontend</b>", verbose_name='Public Display'),
        ),
        migrations.AlterField(
            model_name='genericmodule',
            name='public_display_title',
            field=models.CharField(blank=True, help_text='You should check the previous field for this to work!', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='genericmodule',
            name='second_title',
            field=models.CharField(blank=True, help_text='You should select the <b>focused template</b> for this to work!', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='genericmodule',
            name='selected_template',
            field=models.CharField(choices=[('cartoview_cms/generic_module/generic_module_default.html', 'Default Template'), ('cartoview_cms/generic_module/generic_module_focused.html', 'Focused Template')], default='cartoview_cms/generic_module/generic_module_default.html', max_length=255),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=50))])), ('paragraph', wagtail.core.blocks.RichTextBlock(form_classname='full')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('list', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(), label='Items'))])), ('accordions', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', max_length=50)), ('content', wagtail.core.blocks.RichTextBlock(label='Content'))])), ('image_text_overlay', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))])), ('image_gallery', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), icon='image', label='Image'))])), ('map', wagtail.core.blocks.StructBlock([('map', cartoview_cms.models.streamfields.Blocks.MapChooserBlock(required=True))])), ('separator', cartoview_cms.models.streamfields.Blocks.SeparatorBlock()), ('related_users', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Section title as it appears to the users', label='Title', max_length=200)), ('users', wagtail.core.blocks.ListBlock(cartoview_cms.models.streamfields.Blocks.UserChooserBlock(required=True), label='Users'))])), ('related_module', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Section title as it appears to the users', label='Title', max_length=200)), ('display_size', wagtail.core.blocks.ChoiceBlock(choices=[('1', '1 - Smallest'), ('2', '2'), ('3', '3'), ('4', '4 - Recommended'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12 - Largest')], label='Display Size')), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['cartoview_cms.GenericPage']), label='Items'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='focused',
            field=models.BooleanField(default=False, help_text='You should select the <b>focused template</b> for the Generic Module!.', verbose_name='Focused'),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='is_redirect',
            field=models.BooleanField(default=False, help_text='Redirct to an <b>External</b> link', verbose_name='Redirect External'),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='selected_template',
            field=models.CharField(choices=[('cartoview_cms/generic_module/generic_page_default.html', 'Default Template')], default='cartoview_cms/generic_module/generic_page_default.html', max_length=255),
        ),
        migrations.AlterField(
            model_name='menulink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
    ]
