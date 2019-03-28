from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from .generic_module.GenericPage import GenericPage


@receiver(pre_delete, sender=GenericPage)
def delete_app(sender, instance, **kwargs):
    if instance.app_instance is not None:
        instance.app_instance.delete()
