from .models import Service


def active_services(request):
    return {
        'navbar_services': Service.active_navbar_services()
    }
