from django.db import models


class SiteSettings(models.Model):

    background_image = models.ImageField(
        upload_to='backgrounds/'
    )

    def __str__(self):
        return "Website Settings"
