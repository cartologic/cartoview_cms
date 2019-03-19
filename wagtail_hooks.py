from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models.general.ContentCategory import ContentCategory
from wagtail.wagtailcore import hooks
from django.shortcuts import redirect


class ContentCategoryModelAdmin(ModelAdmin):
    model = ContentCategory
    menu_label = 'Content Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'folder'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ContentCategoryModelAdmin)


@hooks.register('before_serve_document')
def serve_document(document, request):
    # eg. use document.file_extension, document.url, document.filename
    if document.file_extension == 'pdf':
        return redirect(document.file.url)
    # no return means the normal page serve will operate
