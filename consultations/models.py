from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor


class Consultation(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]

    CONFIRMATION_METHODS = [
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('sms', 'SMS'),
        ('call', 'Phone Call'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    confirmation_method = models.CharField(
        max_length=20,
        choices=CONFIRMATION_METHODS,
        default='email'
    )

    confirmation_message = models.TextField(
        blank=True,
        null=True
    )

    confirmation_sent = models.BooleanField(
        default=False
    )

    confirmed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.doctor.name} - "
            f"{self.appointment_date}"
        )