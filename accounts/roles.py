# User Roles and Permissions Management

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

ROLES = {
    'super_admin': {
        'display_name': 'Super Admin',
        'permissions': [
            'add_user', 'change_user', 'delete_user', 'view_user',
            'add_group', 'change_group', 'delete_group', 'view_group',
            'add_permission', 'change_permission', 'delete_permission', 'view_permission',
            'add_userprofile', 'change_userprofile', 'delete_userprofile', 'view_userprofile',
        ]
    },
    'admin': {
        'display_name': 'Admin',
        'permissions': [
            'add_user', 'change_user', 'view_user',
            'add_userprofile', 'change_userprofile', 'view_userprofile',
            'add_product', 'change_product', 'delete_product', 'view_product',
            'add_service', 'change_service', 'delete_service', 'view_service',
            'add_order', 'change_order', 'view_order',
        ]
    },
    'customer': {
        'display_name': 'Customer',
        'permissions': [
            'view_product', 'view_service', 'add_order', 'view_order',
            'add_review', 'change_review', 'delete_review',
        ]
    },
    'doctor': {
        'display_name': 'Plant Doctor',
        'permissions': [
            'add_consultation', 'change_consultation', 'view_consultation',
            'add_review', 'view_review',
        ]
    },
    'gardener': {
        'display_name': 'Gardener',
        'permissions': [
            'add_booking', 'change_booking', 'view_booking',
            'add_review', 'view_review',
        ]
    },
    'seller': {
        'display_name': 'Seller/Vendor',
        'permissions': [
            'add_product', 'change_product', 'delete_product', 'view_product',
            'view_order', 'change_order',
            'add_review', 'view_review',
        ]
    },
    'nursery_owner': {
        'display_name': 'Nursery Owner',
        'permissions': [
            'add_product', 'change_product', 'delete_product', 'view_product',
            'add_service', 'change_service', 'view_service',
            'view_order', 'view_consultation',
            'add_review', 'view_review',
        ]
    },
    'delivery_partner': {
        'display_name': 'Delivery Partner',
        'permissions': [
            'view_order', 'change_order',
        ]
    },
    'consultant': {
        'display_name': 'Agricultural Consultant',
        'permissions': [
            'add_consultation', 'change_consultation', 'view_consultation',
            'view_product', 'view_service',
            'add_review', 'view_review',
        ]
    },
    'vendor': {
        'display_name': 'Vendor',
        'permissions': [
            'add_product', 'change_product', 'delete_product', 'view_product',
            'view_order', 'add_review', 'view_review',
        ]
    },
}


def create_roles_and_permissions():
    """Create all roles and assign permissions"""
    
    for role_key, role_data in ROLES.items():
        group, created = Group.objects.get_or_create(name=role_data['display_name'])
        
        if created:
            print(f"Created group: {role_data['display_name']}")
        
        # Clear existing permissions
        group.permissions.clear()
        
        # Add permissions to group
        for perm_codename in role_data['permissions']:
            try:
                # Try to find the permission
                # First check accounts app
                permission = Permission.objects.filter(codename=perm_codename).first()
                
                if permission:
                    group.permissions.add(permission)
                    print(f"Added permission '{perm_codename}' to group '{group.name}'")
            except Exception as e:
                print(f"Error adding permission '{perm_codename}': {str(e)}")


def get_user_role_display(user):
    """Get user's role as display name"""
    if hasattr(user, 'userprofile'):
        profile = user.userprofile
        for role_key, role_data in ROLES.items():
            if role_key == profile.user_type:
                return role_data['display_name']
    return 'User'


def get_role_dashboard_redirect(user):
    """Get dashboard URL based on user role"""
    
    role_map = {
        'super_admin': 'super_admin_dashboard',
        'admin': 'admin_dashboard',
        'customer': 'customer_dashboard',
        'doctor': 'doctor_dashboard',
        'gardener': 'gardener_dashboard',
        'seller': 'seller_dashboard',
        'nursery_owner': 'nursery_dashboard',
        'delivery_partner': 'delivery_dashboard',
        'consultant': 'consultant_dashboard',
        'vendor': 'vendor_dashboard',
    }
    
    if hasattr(user, 'userprofile'):
        user_type = user.userprofile.user_type
        return role_map.get(user_type, 'home')
    
    return 'home'
