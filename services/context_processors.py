from .models import Service


def active_services(request):
    services = Service.objects.filter(is_active=True, show_in_navbar=True).order_by('title')
    return {
        'navbar_services': services
    }
