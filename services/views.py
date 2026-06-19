from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory


def service_list(request):

    services = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        "services/service_list.html",
        {
            "services": services
        }
    )


def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    return render(
        request,
        "services/service_detail.html",
        {
            "service": service
        }
    )


# temporary category page
def category_services(request, slug):

    category = get_object_or_404(
        ServiceCategory,
        slug=slug,
        is_active=True
    )

    services = Service.objects.filter(
        category=category,
        is_active=True
    )

    return render(
        request,
        "services/service_list.html",
        {
            "services": services,
            "category": category
        }
    )


# temporary booking page
def book_service(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    return render(
        request,
        "services/book_service.html",
        {
            "service": service
        }
    )