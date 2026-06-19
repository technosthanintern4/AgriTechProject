# Decorators for role-based access control

from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def role_required(*allowed_roles):
    """
    Decorator to check if user has specific role.
    
    Usage:
        @role_required('customer', 'seller')
        def my_view(request):
            pass
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapper(request, *args, **kwargs):
            if hasattr(request.user, 'userprofile'):
                user_role = request.user.userprofile.user_type
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            
            return HttpResponseForbidden(
                "You don't have permission to access this page."
            )
        
        return wrapper
    return decorator


def customer_required(view_func):
    """Decorator for customer-only views"""
    return role_required('customer')(view_func)


def doctor_required(view_func):
    """Decorator for doctor-only views"""
    return role_required('doctor')(view_func)


def gardener_required(view_func):
    """Decorator for gardener-only views"""
    return role_required('gardener')(view_func)


def seller_required(view_func):
    """Decorator for seller-only views"""
    return role_required('seller')(view_func)


def nursery_owner_required(view_func):
    """Decorator for nursery owner-only views"""
    return role_required('nursery_owner')(view_func)


def admin_required(view_func):
    """Decorator for admin-only views"""
    return role_required('admin', 'super_admin')(view_func)


def super_admin_required(view_func):
    """Decorator for super admin-only views"""
    return role_required('super_admin')(view_func)


def staff_required(view_func):
    """Decorator for staff users (admin, super_admin)"""
    return role_required('admin', 'super_admin')(view_func)


def seller_or_owner_required(view_func):
    """Decorator for sellers and owners"""
    return role_required('seller', 'nursery_owner')(view_func)
