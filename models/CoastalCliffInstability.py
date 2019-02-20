import json
from django.db import models

from cartoview.app_manager.models import App, AppInstance
from geonode.base.models import TopicCategory
from .BaseGeoPage import BaseGeoPage


class CoastalCliffInstability(BaseGeoPage):
    is_creatable = False
    subpage_types = []
    app_instance = models.OneToOneField(AppInstance, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    category_identifier = "coastalCliffInstability"
    category_description = "Base Category for all CMS Coastal Cliff Instability Topics"
    category_gn_description = "Coastal Cliff Instability"

    def __init__(self, *args, **kwargs):
        super(CoastalCliffInstability, self).__init__(*args, **kwargs)
        BaseGeoPage.assure_category_exists(CoastalCliffInstability.category_identifier, CoastalCliffInstability.category_description,
                                           CoastalCliffInstability.category_gn_description)

    def save(self, *args, **kwargs):
        app = App.objects.filter(name="cartoview_cms").first()
        category = TopicCategory.objects.filter(identifier=self.category_identifier).first()
        thumbnail_url = ""
        self.category = category
        if self.map is not None:
            thumbnail_url = self.map.map_object.thumbnail_url
        if self.app_instance is None:
            app_instance = AppInstance(
                title=self.title,
                config=json.dumps({
                    'title': self.title,
                    'abstract': self.abstract
                }),
                owner=self.owner,
                app=app,
                thumbnail_url=thumbnail_url,
                abstract=self.abstract,
                category=category
            )
            app_instance.save()
            self.app_instance = app_instance
        else:
            app_instance = self.app_instance
            app_instance.title = self.title
            app_instance.config = json.dumps({
                'title': self.title,
                'abstract': self.abstract
            })
            app_instance.owner = self.owner
            app_instance.app = app
            app_instance.thumbnail_url = thumbnail_url
            app_instance.abstract = self.abstract
            app_instance.category = category
            app_instance.save()
        super(CoastalCliffInstability, self).save()

    class Meta:
        verbose_name_plural = 'Coastal Cliff Instability Topics'
