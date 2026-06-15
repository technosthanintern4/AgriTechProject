from .models import SiteSettings


def site_settings(request):

    settings = SiteSettings.objects.order_by('-pk').first()

    return {
        'site_settings': settings
    }