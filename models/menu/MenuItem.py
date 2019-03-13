from wagtailmenus.models import MenuPage


class MenuItem(MenuPage):
    subpage_types = ['cartoview_cms.MenuItem', 'cartoview_cms.MenuLink', 'cartoview_cms.StaticPage',
                     'cartoview_cms.GeoPage', 'cartoview_cms.FormPage', 'cartoview_cms.ContentGroup',
                     'cartoview_cms.CaseStudyIndex', 'cartoview_cms.CountriesIndex', 'cartoview_cms.OrganizationsIndex',
                     'cartoview_cms.TrainingsIndex', 'cartoview_cms.NewsIndex',
                     ]
    show_in_menus_default = True
