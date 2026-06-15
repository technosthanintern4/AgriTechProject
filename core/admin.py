from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import SiteSettings


class SiteSettingsAdminForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'watermark_position': forms.Select(attrs={'style': 'max-width: 320px;'}),
            'watermark_opacity': forms.NumberInput(attrs={
                'min': '0.0',
                'max': '1.0',
                'step': '0.05',
                'style': 'max-width: 120px;'
            }),
        }


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsAdminForm
    fieldsets = (
        ('Background settings', {
            'fields': (
                'background_image',
                'background_video',
                'background_preview',
                'enable_background_video',
            ),
            'description': 'Upload a background image or video. Video is shown when enabled and present.',
        }),
        ('Watermark settings', {
            'fields': (
                'watermark_image',
                'watermark_video',
                'watermark_preview',
                'watermark_position',
                'watermark_opacity',
                'enable_watermark',
            ),
            'description': 'Upload a watermark image or video. Watermark video takes priority if both are present.',
        }),
    )
    readonly_fields = ('background_preview', 'watermark_preview')
    list_display = (
        '__str__',
        'get_background_status',
        'get_watermark_status',
        'enable_background_video',
        'enable_watermark',
    )
    list_display_links = ('__str__',)

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

    def background_preview(self, obj):
        if obj.background_video and obj.enable_background_video:
            return format_html(
                '<video width="320" controls loop muted style="border:1px solid #ddd;border-radius:6px;">'
                '<source src="{}" type="video/mp4">'
                'Your browser does not support video.'</video>',
                obj.background_video.url,
            )
        if obj.background_image:
            return format_html(
                '<img src="{}" style="max-width: 320px; max-height: 180px; border:1px solid #ddd; border-radius:6px;" />',
                obj.background_image.url,
            )
        return 'No background media uploaded.'
    background_preview.short_description = 'Background preview'

    def watermark_preview(self, obj):
        if obj.watermark_video and obj.enable_watermark:
            return format_html(
                '<video width="240" controls loop muted style="border:1px solid #ddd;border-radius:6px;">'
                '<source src="{}" type="video/mp4">'
                'Your browser does not support video.'</video>',
                obj.watermark_video.url,
            )
        if obj.watermark_image:
            return format_html(
                '<img src="{}" style="max-width: 240px; max-height: 180px; border:1px solid #ddd; border-radius:6px;" />',
                obj.watermark_image.url,
            )
        return 'No watermark media uploaded.'
    watermark_preview.short_description = 'Watermark preview'

    def has_add_permission(self, request):
        """Allow only one SiteSettings instance."""
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of SiteSettings"""
        return False