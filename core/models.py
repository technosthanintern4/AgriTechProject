from decimal import Decimal
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.exceptions import ValidationError


def get_video_storage():
    try:
        cloud_name = getattr(settings, 'CLOUDINARY_CLOUD_NAME', None)
        api_key = getattr(settings, 'CLOUDINARY_API_KEY', None)
        api_secret = getattr(settings, 'CLOUDINARY_API_SECRET', None)
        cloudinary_url = getattr(settings, 'CLOUDINARY_URL', None)
    except Exception:
        return FileSystemStorage()

    if cloudinary_url or (cloud_name and api_key and api_secret):
        from cloudinary_storage.storage import VideoMediaCloudinaryStorage
        return VideoMediaCloudinaryStorage()

    return FileSystemStorage()


class SiteSettings(models.Model):
    background_video = models.FileField(
        upload_to='backgrounds/',
        storage=get_video_storage(),
        blank=True,
        null=True,
        help_text='Upload a background video (mp4, webm) to display on the homepage.'
    )

    enable_background_video = models.BooleanField(
        default=False,
        help_text='Enable background video display on the homepage.'
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Website Settings"

