# Generated by Django 2.2.20 on 2021-12-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('coderedcms', '0019_spelling_corrections'),
        ('cartoview_cms', '0003_auto_20211212_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menulink',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='MenuLink',
        ),
    ]
