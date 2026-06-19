from django.urls import path
from .views import (
    dashboard_home,
    super_admin_dashboard,
    admin_dashboard,
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
    path('super-admin/', super_admin_dashboard, name='super_admin_dashboard'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('customer/', customer_dashboard, name='customer_dashboard'),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('gardener/', gardener_dashboard, name='gardener_dashboard'),
    path('seller/', seller_dashboard, name='seller_dashboard'),
    path('nursery/', nursery_dashboard, name='nursery_dashboard'),
    path('delivery/', delivery_dashboard, name='delivery_dashboard'),
    path('consultant/', consultant_dashboard, name='consultant_dashboard'),
    path('vendor/', vendor_dashboard, name='vendor_dashboard'),
]
