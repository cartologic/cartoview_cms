from django.conf.urls import url, include
from wagtail.documents import urls as wagtaildocs_urls
from coderedcms import admin_urls as coderedadmin_urls
from coderedcms import search_urls as coderedsearch_urls
from coderedcms import urls as codered_urls

from . import views

urlpatterns = [
    url(r'^admin/', include(coderedadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(codered_urls)),
    url(r'^search/', include(coderedsearch_urls)),
    url(r'^new/', views.cms.new, name="cartoview_cms.new"),
    url(r'^(?P<instanceid>[^/]*)/view/$', views.cms.view, name='cartoview_cms.view'),
    url(r'^(?P<instanceid>[^/]*)/edit/$', views.cms.edit, name='cartoview_cms.edit'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(codered_urls)),
]

urlpatterns += views.cms.get_url_patterns()
