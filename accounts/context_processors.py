# Context processors for user and dashboard data

from .roles import get_user_role_display, ROLES


def user_context(request):
    """Add user profile and role information to template context"""
    
    context = {
        'is_authenticated': request.user.is_authenticated,
        'user_role': None,
        'user_role_display': None,
        'user_profile': None,
        'is_admin': False,
        'is_super_admin': False,
        'is_customer': False,
        'is_doctor': False,
        'is_gardener': False,
        'is_seller': False,
        'is_nursery_owner': False,
        'is_delivery_partner': False,
        'is_consultant': False,
        'is_vendor': False,
    }
    
    if request.user.is_authenticated:
        if hasattr(request.user, 'userprofile'):
            profile = request.user.userprofile
            context['user_profile'] = profile
            context['user_role'] = profile.user_type
            context['user_role_display'] = get_user_role_display(request.user)
            
            # Set role flags
            context[f'is_{profile.user_type}'] = True
            context['is_staff'] = request.user.is_staff
            context['is_super_admin'] = request.user.is_superuser
            context['is_admin'] = request.user.is_staff or request.user.is_superuser
    
    return context


def dashboard_context(request):
    """Add dashboard-specific data to context"""
    
    context = {
        'dashboard_active': False,
        'available_roles': ROLES,
    }
    
    # Determine if user is on a dashboard page
    if request.path.startswith('/dashboard/'):
        context['dashboard_active'] = True
    
    return context
