from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from geonode.base.models import TopicCategory
from .SeaLevelRise import SeaLevelRise
from .WaterPollution import WaterPollution
from .CoastalCliffInstability import CoastalCliffInstability
from .SeaWaterIntrusion import SeaWaterIntrusion
from .CoastalErosion import CoastalErosion
from .LandSubsidence import LandSubsidence
from .GroundWaterQuality import GroundWaterQuality

from .ContentCategory import ContentCategory
from .GeoPage import GeoPage


@receiver(pre_delete, sender=SeaLevelRise)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=WaterPollution)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=CoastalCliffInstability)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=SeaWaterIntrusion)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=CoastalErosion)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=LandSubsidence)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


@receiver(pre_delete, sender=GroundWaterQuality)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()


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
        GeoPage.assure_category_exists(instance.name)
