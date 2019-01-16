from django.conf.urls import url, include
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from . import views

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),

    url(r'^new/', views.cms.new, name="cartoview_cms.new"),

    url(r'^(?P<instanceid>[^/]*)/view/$', views.cms.view, name='cartoview_cms.view'),
    url(r'^(?P<instanceid>[^/]*)/edit/$', views.cms.edit, name='cartoview_cms.edit'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
]

urlpatterns += views.cms.get_url_patterns()
