from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from geonode.base.models import TopicCategory


class ContentCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    @staticmethod
    def assure_category_exists(category_name):
        identifier = category_name
        description = category_name
        gn_description = category_name
        num_results = TopicCategory.objects.filter(identifier=identifier).count()
        if num_results == 0:
            temp_category = TopicCategory(
                identifier=identifier,
                description=description,
                gn_description=gn_description
            )
            temp_category.save()

    class Meta:
        verbose_name_plural = 'Content Categories'
