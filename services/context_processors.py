from .models import Service


def active_services(request):
    services = Service.objects.filter(is_active=True).order_by('title')
    return {
        'navbar_services': services
    }
