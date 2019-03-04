from wagtailmenus.models import MenuPage


class MenuItem(MenuPage):
    subpage_types = ['cartoview_cms.MenuItem', 'cartoview_cms.MenuLink']
    show_in_menus_default = True
