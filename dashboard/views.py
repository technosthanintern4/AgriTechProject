from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Sum

from accounts.decorators import (
    super_admin_required,
    admin_required,
    role_required,
)
from accounts.roles import get_role_dashboard_redirect

from orders.models import Order
from products.models import Product
from services.models import Service
from consultations.models import Consultation
from wishlist.models import Wishlist
from gardeners.models import GardenerBooking


@login_required
def dashboard_home(request):
    return redirect(get_role_dashboard_redirect(request.user))


def get_base_dashboard_context():
    return {
        'total_users': User.objects.count(),
        'total_orders': Order.objects.count(),
        'total_products': Product.objects.count(),
        'total_services': Service.objects.count(),
        'total_consultations': Consultation.objects.count(),
        'total_bookings': GardenerBooking.objects.count(),
        'active_products': Product.objects.filter(is_available=True).count(),
        'active_services': Service.objects.filter(is_active=True).count(),
        'completed_revenue': Order.objects.filter(is_completed=True).aggregate(total=Sum('total_amount'))['total'] or 0,
    }


@super_admin_required
def super_admin_dashboard(request):
    context = get_base_dashboard_context()
    context.update({
        'dashboard_title': 'Super Admin Dashboard',
        'pending_orders': Order.objects.filter(status='Pending').count(),
        'pending_bookings': GardenerBooking.objects.filter(status='Pending').count(),
        'pending_consultations': Consultation.objects.filter(status='Pending').count(),
    })
    return render(request, 'dashboard/super_admin_dashboard.html', context)


@admin_required
def admin_dashboard(request):
    context = get_base_dashboard_context()
    context.update({
        'dashboard_title': 'Admin Dashboard',
        'recent_orders': Order.objects.order_by('-created_at')[:5],
        'recent_services': Service.objects.order_by('-created_at')[:5],
    })
    return render(request, 'dashboard/admin_dashboard.html', context)


@role_required('customer')
def customer_dashboard(request):
    context = {
        'dashboard_title': 'Customer Dashboard',
        'orders_count': Order.objects.filter(user=request.user).count(),
        'consultations_count': Consultation.objects.filter(user=request.user).count(),
        'bookings_count': GardenerBooking.objects.filter(user=request.user).count(),
        'wishlist_count': Wishlist.objects.filter(user=request.user).count(),
        'recent_orders': Order.objects.filter(user=request.user).order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/customer_dashboard.html', context)


@role_required('doctor')
def doctor_dashboard(request):
    context = {
        'dashboard_title': 'Doctor Dashboard',
        'total_consultations': Consultation.objects.filter(status='Pending').count(),
        'completed_consultations': Consultation.objects.filter(status='Completed').count(),
        'upcoming_appointments': Consultation.objects.filter(status='Approved').order_by('appointment_date')[:5],
    }
    return render(request, 'dashboard/doctor_dashboard.html', context)


@role_required('gardener')
def gardener_dashboard(request):
    context = {
        'dashboard_title': 'Gardener Dashboard',
        'total_bookings': GardenerBooking.objects.count(),
        'confirmed_bookings': GardenerBooking.objects.filter(status='Confirmed').count(),
        'pending_bookings': GardenerBooking.objects.filter(status='Pending').count(),
        'upcoming_jobs': GardenerBooking.objects.filter(status__in=['Pending', 'Confirmed']).order_by('booking_date')[:5],
    }
    return render(request, 'dashboard/gardener_dashboard.html', context)


@role_required('seller')
def seller_dashboard(request):
    context = {
        'dashboard_title': 'Seller Dashboard',
        'total_products': Product.objects.count(),
        'active_products': Product.objects.filter(is_available=True).count(),
        'product_orders': Order.objects.count(),
        'total_revenue': Order.objects.filter(is_completed=True).aggregate(total=Sum('total_amount'))['total'] or 0,
    }
    return render(request, 'dashboard/seller_dashboard.html', context)


@role_required('nursery_owner')
def nursery_dashboard(request):
    context = {
        'dashboard_title': 'Nursery Owner Dashboard',
        'total_products': Product.objects.count(),
        'total_services': Service.objects.count(),
        'active_products': Product.objects.filter(is_available=True).count(),
        'active_services': Service.objects.filter(is_active=True).count(),
    }
    return render(request, 'dashboard/nursery_dashboard.html', context)


@role_required('delivery_partner')
def delivery_dashboard(request):
    context = {
        'dashboard_title': 'Delivery Partner Dashboard',
        'pending_orders': Order.objects.filter(status='Pending').count(),
        'shipped_orders': Order.objects.filter(status='Shipped').count(),
        'delivered_orders': Order.objects.filter(status='Delivered').count(),
    }
    return render(request, 'dashboard/delivery_dashboard.html', context)


@role_required('consultant')
def consultant_dashboard(request):
    context = {
        'dashboard_title': 'Consultant Dashboard',
        'total_consultations': Consultation.objects.count(),
        'approved_consultations': Consultation.objects.filter(status='Approved').count(),
        'pending_consultations': Consultation.objects.filter(status='Pending').count(),
    }
    return render(request, 'dashboard/consultant_dashboard.html', context)


@role_required('vendor')
def vendor_dashboard(request):
    context = {
        'dashboard_title': 'Vendor Dashboard',
        'total_products': Product.objects.count(),
        'active_products': Product.objects.filter(is_available=True).count(),
        'orders_count': Order.objects.count(),
    }
    return render(request, 'dashboard/vendor_dashboard.html', context)
