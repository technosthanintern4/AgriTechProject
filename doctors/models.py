from django.db import models


class Doctor(models.Model):

    name = models.CharField(
        max_length=200
    )

    specialization = models.CharField(
        max_length=200
    )

    experience = models.IntegerField()

    image = models.ImageField(
        upload_to='doctors/'
    )

    bio = models.TextField()

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
