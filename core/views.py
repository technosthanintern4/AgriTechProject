from django.shortcuts import render
from cms.models import HomePageContent
from services.models import Service


def home(request):
    services = Service.objects.filter(
        is_active=True
    ).order_by('title')

    return render(
        request,
        "core/home.html",
        {
            "services": services,
            "home_content": HomePageContent.objects.filter(is_active=True).first(),
        }
    )
