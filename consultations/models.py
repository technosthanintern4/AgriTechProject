from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
from cloudinary.models import CloudinaryField


class Consultation(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    plant_name = models.CharField(
        max_length=255
    )

    disease_description = models.TextField()

    image = CloudinaryField(
        'image',
    )


    appointment_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.plant_name