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
    site_name = models.CharField(max_length=150, default='AgroSthan')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    footer_logo = models.ImageField(upload_to='site/', blank=True, null=True)
    contact_details = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    copyright_text = models.CharField(
        max_length=255,
        default='© 2026 AgroSthan. All Rights Reserved.'
    )

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

