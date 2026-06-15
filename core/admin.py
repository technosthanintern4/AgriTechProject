from django.contrib import admin

from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Background settings', {
            'classes': ('wide',),
            'fields': (
                'background_image',
                'background_video',
                'enable_background_video',
            ),
            'description': 'Upload a background image or video. Video will display when enabled and present.',
        }),
        ('Watermark settings', {
            'classes': ('wide',),
            'fields': (
                'watermark_image',
                'watermark_video',
                'watermark_position',
                'watermark_opacity',
                'enable_watermark',
            ),
            'description': 'Upload a watermark image or video. Watermark image is used unless watermark video is enabled and present.',
        }),
    )
    list_display = (
        '__str__',
        'get_background_status',
        'get_watermark_status',
        'enable_background_video',
        'enable_watermark',
    )
    list_display_links = ('__str__',)
    list_per_page = 20
    save_on_top = True

    def get_background_status(self, obj):
        if obj.background_video and obj.enable_background_video:
            return 'Video'
        if obj.background_image:
            return 'Image'
        return 'Default'
    get_background_status.short_description = 'Background'

    def get_watermark_status(self, obj):
        if obj.enable_watermark:
            return 'Enabled'
        return 'Disabled'
    get_watermark_status.short_description = 'Watermark'

    def has_add_permission(self, request):
        """Allow only one SiteSettings instance."""
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of SiteSettings"""
        return False