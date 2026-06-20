import logging

from .models import SiteSettings


logger = logging.getLogger(__name__)


def site_settings(request):

    try:
        settings = SiteSettings.objects.order_by('-pk').first()
    except Exception:
        logger.exception("Failed to load site settings")
        settings = None

    return {
        'site_settings': settings
    }
