PROJECT_DIR = CARTOVIEW_DIR

MIDDLEWARE += (
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

INSTALLED_APPS += (
    # CodeRed CMS
    'coderedcms',
    'bootstrap4',
    'modelcluster',
    'wagtailmenus',
    'wagtailfontawesome',
    'wagtailcache',
    'wagtailimportexport',

    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.core',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
    'wagtail.admin',
)

CARTOVIEW_CMS_CONTEXT_PROCESSORS = ('wagtailmenus.context_processors.wagtailmenus',)

TEMPLATES[0]["OPTIONS"]['context_processors'] += CARTOVIEW_CMS_CONTEXT_PROCESSORS

# SITE_NAME declared at cartoview.settings.py
WAGTAIL_SITE_NAME = "CMS"

# Bootstrap
BOOTSTRAP4 = {
    # set to blank since coderedcms already loads jquery and bootstrap
    'jquery_url': '',
    'base_url': '',
    # remove green highlight on inputs
    'success_css_class': ''
}

# Tags
TAGGIT_CASE_INSENSITIVE = True
