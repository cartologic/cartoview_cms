from wagtailmenus.models import MenuPage


class MenuItem(MenuPage):
    subpage_types = ['cartoview_cms.MenuItem', 'cartoview_cms.MenuLink', 'cartoview_cms.StaticPage',
                     'cartoview_cms.GeoPage', 'cartoview_cms.FormPage', 'cartoview_cms.ContentGroup',
                     'cartoview_cms.CaseStudyIndex',
                     ]
    show_in_menus_default = True
