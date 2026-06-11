from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Gardener(models.Model):

    name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=15
    )

    experience = models.PositiveIntegerField(
        help_text="Experience in Years"
    )

    specialization = models.CharField(
        max_length=255
    )

    image = CloudinaryField(
        'image'
    )

    daily_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name