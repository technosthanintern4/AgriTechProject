from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory
from datetime import datetime


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

    # Get today's date for the date picker minimum value
    today_date = datetime.now().strftime('%Y-%m-%d')

    # Handle form submission
    if request.method == 'POST':
        # Process booking form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        consultation_type = request.POST.get('type')
        message = request.POST.get('message')
        
        # TODO: Save booking to database or send email notification
        # For now, redirect to a success page or show a success message
        
        # Temporary success handling
        context = {
            'service': service,
            'today_date': today_date,
            'booking_success': True,
            'booking_details': {
                'name': name,
                'email': email,
                'phone': phone,
                'date': date,
                'time': time,
                'type': consultation_type
            }
        }
    else:
        context = {
            'service': service,
            'today_date': today_date
        }

    return render(
        request,
        "services/book_service.html",
        context
    )