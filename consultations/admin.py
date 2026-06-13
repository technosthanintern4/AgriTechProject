from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .models import Consultation


@admin.action(description="Send confirmation email to selected users")
def send_confirmation_email(modeladmin, request, queryset):

    for consultation in queryset:

        if consultation.confirmation_method == "email":

            message = consultation.confirmation_message

            if not message:

                message = (
                    f"Hello {consultation.user.username},\n\n"
                    f"Your appointment with Dr. {consultation.doctor.name} "
                    f"has been confirmed.\n\n"
                    f"Appointment Date: {consultation.appointment_date}\n\n"
                    f"Thank you,\n"
                    f"AgriTech Nursery"
                )

            send_mail(
                subject="Appointment Confirmation",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[consultation.user.email],
                fail_silently=False
            )

            consultation.confirmation_sent = True
            consultation.confirmed_at = timezone.now()
            consultation.save()


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):

    actions = [send_confirmation_email]

    list_display = [
        'user',
        'doctor',
        'appointment_date',
        'status',
        'confirmation_method',
        'confirmation_sent',
        'created_at'
    ]

    list_filter = [
        'status',
        'confirmation_method',
        'confirmation_sent'
    ]

    search_fields = [
        'user__username',
        'doctor__name'
    ]

    fieldsets = (

        (
            'Consultation Details',
            {
                'fields': (
                    'user',
                    'doctor',
                    'appointment_date',
                    'status'
                )
            }
        ),

        (
            'Confirmation Settings',
            {
                'fields': (
                    'confirmation_method',
                    'confirmation_message',
                    'confirmation_sent',
                    'confirmed_at'
                )
            }
        ),

    )