from .models import Service


def active_services(request):
    """
    Context processor to provide active services for navbar.
    """
    return {
        'navbar_services': Service.active_navbar_services()
    }
