from django.db import models
from cloudinary.models import CloudinaryField


class DoctorCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doctor Category'
        verbose_name_plural = 'Doctor Categories'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    category = models.ForeignKey(
        DoctorCategory,
        on_delete=models.SET_NULL,
        related_name='doctors',
        blank=True,
        null=True
    )

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
    availability = models.TextField(blank=True)
    consultation_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DoctorAvailability(models.Model):
    WEEKDAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availability_slots')
    weekday = models.CharField(max_length=20, choices=WEEKDAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['doctor', 'weekday', 'start_time']
        verbose_name = 'Doctor Availability'
        verbose_name_plural = 'Doctor Availability'

    def __str__(self):
        return f"{self.doctor.name} - {self.get_weekday_display()}"
