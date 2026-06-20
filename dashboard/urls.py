from django.urls import path
from .views import (
    dashboard_home,
    customer_dashboard,
    doctor_dashboard,
    gardener_dashboard,
    seller_dashboard,
    nursery_dashboard,
    delivery_dashboard,
    consultant_dashboard,
    vendor_dashboard,
)

urlpatterns = [
    path('', dashboard_home, name='dashboard_home'),
    path('customer/', customer_dashboard, name='customer_dashboard'),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('gardener/', gardener_dashboard, name='gardener_dashboard'),
    path('seller/', seller_dashboard, name='seller_dashboard'),
    path('nursery/', nursery_dashboard, name='nursery_dashboard'),
    path('delivery/', delivery_dashboard, name='delivery_dashboard'),
    path('consultant/', consultant_dashboard, name='consultant_dashboard'),
    path('vendor/', vendor_dashboard, name='vendor_dashboard'),
]
