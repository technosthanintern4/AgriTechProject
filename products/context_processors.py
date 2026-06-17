from .models import ProductCategory


def navbar_categories(request):
    categories = ProductCategory.objects.filter(
        is_active=True
    ).order_by('name')

    return {
        'navbar_categories': categories
    }