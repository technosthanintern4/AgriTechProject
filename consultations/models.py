from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
from services.models import Service


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
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='consultations'
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

    # Service-specific details
    animal_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Type of pet/animal (e.g., Dog, Cat, Goat, Cow)"
    )

    animal_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Name of the pet/animal"
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description of issue or service needed"
    )

    area_size = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Area size for gardening services (e.g., 1000 sqft)"
    )

    duration = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Duration for contract gardening (e.g., 3 months, 1 year)"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        target = self.doctor.name if self.doctor else (self.service.title if self.service else 'N/A')
        return (
            f"{self.user.username} - "
            f"{target} - "
            f"{self.appointment_date}"
        )


class NotificationLog(models.Model):

    METHODS = [
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('sms', 'SMS'),
        ('call', 'Phone Call'),
    ]

    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    method = models.CharField(
        max_length=20,
        choices=METHODS
    )

    message = models.TextField()

    success = models.BooleanField(
        default=True
    )

    sent_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.method}"
        )