from django.shortcuts import render
from services.models import Service


def home(request):
    services = Service.active_navbar_services()

    return render(
        request,
        "core/home.html",
        {
            "services": services
        }
    )