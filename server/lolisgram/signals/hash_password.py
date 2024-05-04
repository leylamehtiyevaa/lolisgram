from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.user_model import CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_hash_password(sender, instance, created, **kwargs):
    """
    Creates a hash password for the user after it is created.
    """
    if created:
        instance.set_password(instance.password)
        instance.save()