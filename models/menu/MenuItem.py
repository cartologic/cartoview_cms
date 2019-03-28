from wagtailmenus.models import MenuPage


class MenuItem(MenuPage):
    subpage_types = [
        'cartoview_cms.MenuItem', 'cartoview_cms.MenuLink', 'cartoview_cms.FormPage',
        'cartoview_cms.GenericModule', 'cartoview_cms.GenericPage'
    ]
    show_in_menus_default = True
