from django.db import models


class SiteSettings(models.Model):

    background_image = models.ImageField(
        upload_to='backgrounds/'
    )

    background_video = models.FileField(
        upload_to='backgrounds/',
        blank=True,
        null=True,
        help_text='Upload a background video (mp4). If present, video will be shown instead of image.'
    )

    def __str__(self):
        return "Website Settings"
