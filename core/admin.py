from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Background Settings', {
            'fields': ('background_image', 'background_video', 'enable_background_video')
        }),
        ('Watermark Image Settings', {
            'fields': ('watermark_image', 'watermark_position', 'watermark_opacity', 'enable_watermark')
        }),
        ('Watermark Video Settings', {
            'fields': ('watermark_video',)
        }),
    )

    list_display = ['__str__', 'enable_watermark', 'enable_background_video']

    def has_add_permission(self, request):
        """Allow only one SiteSettings instance."""
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of SiteSettings"""
        return False