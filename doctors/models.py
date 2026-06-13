from django.db import models
from cloudinary.models import CloudinaryField


class Doctor(models.Model):

    name = models.CharField(max_length=200)

    specialization = models.CharField(max_length=200)

    experience = models.IntegerField()

    image = CloudinaryField('image')

    bio = models.TextField()

    is_available = models.BooleanField(default=True)

    fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name