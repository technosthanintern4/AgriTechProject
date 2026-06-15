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
    # Background Settings
    background_image = models.ImageField(
        upload_to='backgrounds/',
        blank=True,
        null=True,
        help_text='Upload a background image. Recommended size: 1920x1080px'
    )

    background_video = models.FileField(
        upload_to='backgrounds/',
        storage=get_video_storage(),
        blank=True,
        null=True,
        help_text='Upload a background video (mp4, webm). If present, video will be shown instead of image.'
    )

    # Watermark Settings
    watermark_image = models.ImageField(
        upload_to='watermarks/',
        blank=True,
        null=True,
        help_text='Upload an image as watermark (PNG recommended for transparency). Size: 200x200px or smaller.'
    )

    watermark_video = models.FileField(
        upload_to='watermarks/',
        storage=get_video_storage(),
        blank=True,
        null=True,
        help_text='Upload a video as watermark (mp4, webm). If both image and video are present, video takes priority.'
    )

    watermark_position = models.CharField(
        max_length=20,
        choices=[
            ('top-left', 'Top Left'),
            ('top-center', 'Top Center'),
            ('top-right', 'Top Right'),
            ('middle-left', 'Middle Left'),
            ('center', 'Center'),
            ('middle-right', 'Middle Right'),
            ('bottom-left', 'Bottom Left'),
            ('bottom-center', 'Bottom Center'),
            ('bottom-right', 'Bottom Right'),
        ],
        default='bottom-right',
        help_text='Position of the watermark on the page'
    )

    watermark_opacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('0.80'),
        help_text='Opacity of watermark (0.0 to 1.0)'
    )

    enable_watermark = models.BooleanField(
        default=False,
        help_text='Enable watermark display on the website'
    )

    enable_background_video = models.BooleanField(
        default=False,
        help_text='Enable background video display (if video is uploaded)'
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Website Settings"

    def clean(self):
        super().clean()
        opacity = self.watermark_opacity
        if opacity is None:
            return

        try:
            opacity_value = float(opacity)
        except (TypeError, ValueError):
            raise ValidationError({
                'watermark_opacity': 'Watermark opacity must be a number between 0.0 and 1.0.'
            })

        if opacity_value < 0 or opacity_value > 1:
            raise ValidationError({
                'watermark_opacity': 'Watermark opacity must be between 0.0 and 1.0.'
            })
