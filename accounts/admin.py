from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserChangeForm, RegisterForm
from .models import UserProfile

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