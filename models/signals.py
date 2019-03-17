from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from geonode.base.models import TopicCategory

from .general.ContentCategory import ContentCategory
from .general.GeoPage import GeoPage


@receiver(pre_delete, sender=GeoPage)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=ContentCategory)
def delete_app(sender, instance, **kwargs):
    if instance.name is not None:
        category = TopicCategory.objects.filter(identifier=instance.name).first()
        if category is not None:
            category.delete()


@receiver(post_save, sender=ContentCategory)
def delete_app(sender, instance, **kwargs):
    if instance.name is not None:
        ContentCategory.assure_category_exists(instance.name)
