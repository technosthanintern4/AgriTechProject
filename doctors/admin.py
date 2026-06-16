from django.contrib import admin
from django.utils.html import format_html
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'image_tag',
        'name',
        'specialization',
        'experience',
        'fees',
        'is_available'
    ]

    readonly_fields = ('image_tag',)

    fieldsets = (
        (None, {
            'fields': (
                'image',
                'name',
                'specialization',
                'experience',
                'fees',
                'is_available',
                'bio',
            )
        }),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:6px;" />',
                obj.image.url
            )
        return '-'

    image_tag.short_description = 'Photo'

    def admin_actions(self, obj):
        detail_url = f"/doctors/{obj.id}/"
        book_url = f"/consultations/book/{obj.id}/"
        return format_html(
            '<a class="button" href="{}" target="_blank">Details</a>&nbsp;'
            '<a class="button btn-info" href="{}" target="_blank">Book</a>',
            detail_url,
            book_url
        )

    admin_actions.short_description = 'Actions'