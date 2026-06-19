from django.shortcuts import render
from services.models import Service


def home(request):
    services = Service.objects.filter(
        is_active=True
    ).order_by('title')

    return render(
        request,
        "core/home.html",
        {
            "services": services
        }
    )