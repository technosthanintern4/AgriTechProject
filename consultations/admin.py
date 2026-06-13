from django.contrib import admin
from .models import Consultation


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):

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