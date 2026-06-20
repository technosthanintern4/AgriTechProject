from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import DatabaseError

from .models import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile when a new User is created"""
    if created:
        try:
            UserProfile.objects.get_or_create(user=instance)
        except DatabaseError:
            return


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """Save UserProfile when User is saved (optional)"""
    try:
        profile = getattr(instance, 'userprofile', None)
    except (UserProfile.DoesNotExist, DatabaseError):
        return

    if profile:
        try:
            profile.save()
        except DatabaseError:
            return
