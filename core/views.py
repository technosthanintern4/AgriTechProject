from django.shortcuts import render
from services.models import Service


def home(request):
    services = Service.objects.filter(
        is_active=True,
        show_in_navbar=True
    )

    return render(
        request,
        "home.html",
        {
            "services": services
        }
    )