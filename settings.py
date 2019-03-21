MIDDLEWARE_CLASSES += (
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

INSTALLED_APPS += (
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.modeladmin',

    'modelcluster',

    'wagtailmenus',
    'widget_tweaks',
    'wagtailfontawesome',
)

CARTOVIEW_CMS_CONTEXT_PROCESSORS = ('wagtailmenus.context_processors.wagtailmenus',)

TEMPLATES[0]["OPTIONS"]['context_processors'] += CARTOVIEW_CMS_CONTEXT_PROCESSORS

WAGTAIL_SITE_NAME = 'CMS'
