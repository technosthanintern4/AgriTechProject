import logging

logger = logging.getLogger(__name__)


def navbar_services(request):

    try:
        from .models import ServiceCategory

        categories = ServiceCategory.objects.filter(
            is_active=True
        ).order_by('name')
    except Exception:
        logger.exception("Failed to load navbar service categories")
        categories = []

    return {
        'navbar_services': categories
    }
