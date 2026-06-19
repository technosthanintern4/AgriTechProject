from .models import ServiceCategory


def navbar_services(request):

    categories = ServiceCategory.objects.filter(
        is_active=True
    ).order_by('name')

    return {
        'navbar_services': categories
    }
