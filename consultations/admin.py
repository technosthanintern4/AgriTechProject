from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .models import Consultation, NotificationLog


@admin.action(description="Send confirmation to selected users")
def send_confirmation(modeladmin, request, queryset):

    for consultation in queryset:

        message = consultation.confirmation_message

        if not message:
            if consultation.doctor:
                appointment_target = f"Dr. {consultation.doctor.name}"
            elif consultation.service:
                appointment_target = consultation.service.title
            else:
                appointment_target = "AgroSthan"

            message = (
                f"Hello {consultation.user.username},\n\n"
                f"Your appointment with {appointment_target} "
                f"has been confirmed.\n\n"
                f"Appointment Date: {consultation.appointment_date}\n\n"
                f"Thank you,\n"
                f"AgroSthan"
            )

        success = True

        try:

            if consultation.confirmation_method == "email":

                send_mail(
                    subject="Appointment Confirmation",
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[consultation.user.email],
                    fail_silently=False
                )

            elif consultation.confirmation_method == "whatsapp":

                # WhatsApp API code later
                pass

            elif consultation.confirmation_method == "sms":

                # SMS API code later
                pass

            elif consultation.confirmation_method == "call":

                # Calling API code later
                pass

        except Exception:
            success = False

        consultation.confirmation_sent = success
        consultation.confirmed_at = timezone.now()
        consultation.save()

        NotificationLog.objects.create(
            consultation=consultation,
            user=consultation.user,
            method=consultation.confirmation_method,
            message=message,
            success=success
        )


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):

    actions = [send_confirmation]

    list_display = [
        'user',
        'doctor',
        'service',
        'appointment_date',
        'appointment_time',
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
        'doctor__name',
        'service__title'
    ]

    fieldsets = (

        (
            'Consultation Details',
            {
                'fields': (
                    'user',
                    'doctor',
                    'service',
                    'appointment_date',
                    'appointment_time',
                    'status'
                )
            }
        ),

        (
            'Patient Details',
            {
                'fields': (
                    'patient_name',
                    'patient_phone',
                    'patient_email',
                    'reports',
                    'notes',
                )
            }
        ),

        (
            'Service Details',
            {
                'fields': (
                    'animal_type',
                    'animal_name',
                    'description',
                    'area_size',
                    'duration'
                ),
                'classes': ('collapse',)
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


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'consultation',
        'method',
        'success',
        'sent_at'
    ]

    list_filter = [
        'method',
        'success'
    ]

    search_fields = [
        'user__username'
    ]
