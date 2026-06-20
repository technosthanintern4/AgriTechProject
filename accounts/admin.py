from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserChangeForm, RegisterForm
from .models import AdminRegistrationCode, UserProfile

User = get_user_model()


class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
	add_form = RegisterForm
	form = CustomUserChangeForm
	model = User
	list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
	list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		('Personal info', {'fields': ('role', 'phone', 'address', 'city', 'state', 'pincode')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_active', 'is_staff')
		}),
	)
	search_fields = ('username', 'email')
	ordering = ('username',)
	inlines = (UserProfileInline,)


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)


@admin.register(AdminRegistrationCode)
class AdminRegistrationCodeAdmin(admin.ModelAdmin):
	list_display = (
		'code',
		'is_active',
		'created_by',
		'expires_at',
		'usage_limit',
		'used_count',
		'created_at',
	)
	list_filter = ('is_active', 'expires_at', 'created_at')
	search_fields = ('code', 'created_by__username', 'created_by__email')
	readonly_fields = ('created_by', 'created_at', 'used_count')
	fieldsets = (
		('Code', {
			'fields': ('code', 'is_active')
		}),
		('Usage Controls', {
			'fields': ('expires_at', 'usage_limit', 'used_count')
		}),
		('Audit', {
			'fields': ('created_by', 'created_at')
		}),
	)

	def _can_manage_admin_codes(self, request):
		return request.user.is_superuser or getattr(request.user, 'role', None) in {
			User.ROLE_SUPER_ADMIN,
			User.ROLE_ADMIN,
		}

	def has_module_permission(self, request):
		return self._can_manage_admin_codes(request) and super().has_module_permission(request)

	def has_view_permission(self, request, obj=None):
		return self._can_manage_admin_codes(request) and super().has_view_permission(request, obj)

	def has_add_permission(self, request):
		return self._can_manage_admin_codes(request) and super().has_add_permission(request)

	def has_change_permission(self, request, obj=None):
		return self._can_manage_admin_codes(request) and super().has_change_permission(request, obj)

	def has_delete_permission(self, request, obj=None):
		return self._can_manage_admin_codes(request) and super().has_delete_permission(request, obj)

	def save_model(self, request, obj, form, change):
		if not obj.created_by_id:
			obj.created_by = request.user
		super().save_model(request, obj, form, change)
