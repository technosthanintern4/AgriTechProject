from django.shortcuts import render
from services.models import Service

def home(request):
    services = Service.objects.filter(is_active=True)[:3]
    return render(request, 'core/home.html', {'services': services})