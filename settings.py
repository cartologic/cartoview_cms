MIDDLEWARE += (
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

INSTALLED_APPS += (
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',

    'modelcluster',

    'wagtailmenus',
    'widget_tweaks',
    'wagtailfontawesome',
)

CARTOVIEW_CMS_CONTEXT_PROCESSORS = ('wagtailmenus.context_processors.wagtailmenus',)

TEMPLATES[0]["OPTIONS"]['context_processors'] += CARTOVIEW_CMS_CONTEXT_PROCESSORS

WAGTAIL_SITE_NAME = 'CMS'
