from django.contrib import admin

from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Website settings', {
            'fields': (
                'site_name',
                'logo',
                'favicon',
                'footer_logo',
                'contact_details',
                'email',
                'phone',
                'address',
                'facebook_url',
                'instagram_url',
                'twitter_url',
                'linkedin_url',
                'youtube_url',
                'copyright_text',
            ),
        }),
        ('Background video', {
            'classes': ('wide',),
            'fields': (
                'background_video',
                'enable_background_video',
            ),
            'description': 'Upload a background video and enable it to display on the homepage.',
        }),
    )
    list_display = (
        '__str__',
        'get_background_status',
        'enable_background_video',
    )
    list_display_links = ('__str__',)
    list_per_page = 20
    save_on_top = True

    def get_background_status(self, obj):
        if obj.background_video and obj.enable_background_video:
            return 'Video'
        return 'Default'
    get_background_status.short_description = 'Background'

    def has_add_permission(self, request):
        """Allow only one SiteSettings instance."""
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of SiteSettings"""
        return False
