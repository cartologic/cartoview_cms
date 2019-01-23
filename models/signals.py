from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .SeaLevelRise import SeaLevelRise
from .WaterPollution import WaterPollution
from .CoastalCliffInstability import CoastalCliffInstability


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
