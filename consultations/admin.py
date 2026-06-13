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

            message = (
                f"Hello {consultation.user.username},\n\n"
                f"Your appointment with Dr. {consultation.doctor.name} "
                f"has been confirmed.\n\n"
                f"Appointment Date: {consultation.appointment_date}\n\n"
                f"Thank you,\n"
                f"AgriTech Nursery"
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