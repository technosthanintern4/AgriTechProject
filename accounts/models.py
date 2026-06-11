from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    USER_TYPES = [
        ('customer', 'Customer'),
        ('gardener', 'Gardener'),
        ('doctor', 'Doctor'),
        ('seller', 'Seller'),
        ('nursery_owner', 'Nursery Owner'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='customer'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    pincode = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_user_type_display()})"