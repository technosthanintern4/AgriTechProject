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
            'add_group', 'change_group', 'delete_group', 'view_group',
            'add_userprofile', 'change_userprofile', 'view_userprofile',
            'add_product', 'change_product', 'delete_product', 'view_product',
            'add_productcategory', 'change_productcategory', 'delete_productcategory', 'view_productcategory',
            'add_productimage', 'change_productimage', 'delete_productimage', 'view_productimage',
            'add_productvariant', 'change_productvariant', 'delete_productvariant', 'view_productvariant',
            'add_service', 'change_service', 'delete_service', 'view_service',
            'add_servicecategory', 'change_servicecategory', 'delete_servicecategory', 'view_servicecategory',
            'add_order', 'change_order', 'view_order',
            'add_consultation', 'change_consultation', 'delete_consultation', 'view_consultation',
            'add_doctor', 'change_doctor', 'delete_doctor', 'view_doctor',
            'add_doctorcategory', 'change_doctorcategory', 'delete_doctorcategory', 'view_doctorcategory',
            'add_doctoravailability', 'change_doctoravailability', 'delete_doctoravailability', 'view_doctoravailability',
            'add_websitesettings', 'change_websitesettings', 'delete_websitesettings', 'view_websitesettings',
            'add_menuitem', 'change_menuitem', 'delete_menuitem', 'view_menuitem',
            'add_homepagecontent', 'change_homepagecontent', 'delete_homepagecontent', 'view_homepagecontent',
            'add_footercontent', 'change_footercontent', 'delete_footercontent', 'view_footercontent',
            'add_dynamicsection', 'change_dynamicsection', 'delete_dynamicsection', 'view_dynamicsection',
            'add_cmspage', 'change_cmspage', 'delete_cmspage', 'view_cmspage',
            'add_blogcategory', 'change_blogcategory', 'delete_blogcategory', 'view_blogcategory',
            'add_tag', 'change_tag', 'delete_tag', 'view_tag',
            'add_blog', 'change_blog', 'delete_blog', 'view_blog',
            'add_mediaasset', 'change_mediaasset', 'delete_mediaasset', 'view_mediaasset',
            'add_department', 'change_department', 'delete_department', 'view_department',
            'add_designation', 'change_designation', 'delete_designation', 'view_designation',
            'add_employee', 'change_employee', 'delete_employee', 'view_employee',
            'add_employeedocument', 'change_employeedocument', 'delete_employeedocument', 'view_employeedocument',
            'add_attendance', 'change_attendance', 'delete_attendance', 'view_attendance',
            'add_task', 'change_task', 'delete_task', 'view_task',
            'add_taskcomment', 'change_taskcomment', 'delete_taskcomment', 'view_taskcomment',
            'add_taskattachment', 'change_taskattachment', 'delete_taskattachment', 'view_taskattachment',
            'add_report', 'change_report', 'delete_report', 'view_report',
        ]
    },
    'employee': {
        'display_name': 'Employee',
        'permissions': [
            'view_task', 'change_task',
            'add_taskcomment', 'view_taskcomment',
            'add_attendance', 'change_attendance', 'view_attendance',
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


ROLE_GROUP_NAMES = [role_data['display_name'] for role_data in ROLES.values()]


def get_role_group_name(role_key):
    """Return the group name for the given role key."""
    return ROLES.get(role_key, {}).get('display_name')


def assign_user_to_role_group(user):
    """Assign the user to the matching role group and remove previous role groups."""
    role = getattr(user, 'role', None)
    if not role:
        return

    group_name = get_role_group_name(role)
    if not group_name:
        return

    current_groups = Group.objects.filter(name__in=ROLE_GROUP_NAMES)
    if current_groups.exists():
        user.groups.remove(*current_groups)

    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"Created role group: {group_name}")
    user.groups.add(group)


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
                permission = Permission.objects.filter(codename=perm_codename).first()
                
                if permission:
                    group.permissions.add(permission)
                    print(f"Added permission '{perm_codename}' to group '{group.name}'")
            except Exception as e:
                print(f"Error adding permission '{perm_codename}': {str(e)}")


def get_user_role_display(user):
    """Get user's role as display name"""
    # Prefer direct user.role (new custom User). Fallback to profile.user_type.
    if hasattr(user, 'role') and user.role:
        return dict((k, v['display_name']) for k, v in ROLES.items()).get(user.role, 'User')
    if hasattr(user, 'userprofile'):
        profile = user.userprofile
        for role_key, role_data in ROLES.items():
            if role_key == getattr(profile, 'user_type', None):
                return role_data['display_name']
    return 'User'


def get_role_dashboard_redirect(user):
    """Get dashboard URL based on user role"""
    
    role_map = {
        'super_admin': 'admin:index',
        'admin': 'admin:index',
        'employee': 'dashboard_home',
        'customer': 'customer_dashboard',
        'doctor': 'doctor_dashboard',
        'gardener': 'gardener_dashboard',
        'seller': 'seller_dashboard',
        'nursery_owner': 'nursery_dashboard',
        'delivery_partner': 'delivery_dashboard',
        'consultant': 'consultant_dashboard',
        'vendor': 'vendor_dashboard',
    }
    
    # Check new User.role first
    if hasattr(user, 'role') and user.role:
        return role_map.get(user.role, 'home')
    if hasattr(user, 'userprofile'):
        user_type = getattr(user.userprofile, 'user_type', None)
        return role_map.get(user_type, 'home')
    
    return 'home'
