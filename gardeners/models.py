from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Gardener(models.Model):

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    experience = models.PositiveIntegerField(
        help_text="Experience in Years"
    )

    specialization = models.CharField(
        max_length=255
    )

    image = CloudinaryField('image')

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


class GardenerBooking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
    ]

    SERVICE_CHOICES = [
        ('Plant Care', 'Plant Care'),
        ('Garden Setup', 'Garden Setup'),
        ('Lawn Maintenance', 'Lawn Maintenance'),
        ('Landscaping', 'Landscaping'),
        ('Pot Replacement', 'Pot Replacement'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    gardener = models.ForeignKey(
        Gardener,
        on_delete=models.CASCADE
    )

    service_type = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    booking_date = models.DateField()

    address = models.TextField()

    notes = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.gardener.name}"