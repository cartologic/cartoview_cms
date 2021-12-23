from wagtail.core import hooks
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from django.shortcuts import redirect
from geonode.maps.models import Map


@hooks.register('before_serve_document')
def serve_document(document, request):
    # eg. use document.file_extension, document.url, document.filename
    if document.file_extension == 'pdf':
        return redirect(document.file.url)
    # no return means the normal page serve will operate


class MapModelPermissionHelper(PermissionHelper):
    """
    List MapModel instances only without create, edit, and delete.
    """

    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        return False

    def user_can_edit_obj(self, user, obj):
        return False

    def user_can_delete_obj(self, user, obj):
        return False


class MapModelAdmin(ModelAdmin):
    """
    Define MapModel for wagtail admin menus.
    """

    model = Map
    menu_label = 'Maps'
    menu_icon = 'site'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'projection', 'created', 'owner')
    list_filter = ('title', 'projection', 'created', 'owner__username')
    permission_helper_class = MapModelPermissionHelper


modeladmin_register(MapModelAdmin)
