import logging

from .models import ProductCategory


logger = logging.getLogger(__name__)

def navbar_categories(request):
    try:
        categories = ProductCategory.objects.filter(
            is_active=True
        ).order_by('name')

    except Exception:
        logger.exception("Failed to load navbar product categories")
        categories = []

    return {
        "navbar_categories": categories
    }
