from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        if not email:
            raise ValueError(_('The email address must be set'))

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    ROLE_SUPER_ADMIN = 'super_admin'
    ROLE_ADMIN = 'admin'
    ROLE_EMPLOYEE = 'employee'
    ROLE_CUSTOMER = 'customer'
    ROLE_DOCTOR = 'doctor'
    ROLE_GARDENER = 'gardener'
    ROLE_SELLER = 'seller'
    ROLE_NURSERY_OWNER = 'nursery_owner'
    ROLE_DELIVERY_PARTNER = 'delivery_partner'
    ROLE_CONSULTANT = 'consultant'
    ROLE_VENDOR = 'vendor'

    ROLE_CHOICES = [
        (ROLE_SUPER_ADMIN, 'Super Admin'),
        (ROLE_ADMIN, 'Admin'),
        (ROLE_EMPLOYEE, 'Employee'),
        (ROLE_CUSTOMER, 'Customer'),
        (ROLE_DOCTOR, 'Doctor'),
        (ROLE_GARDENER, 'Gardener'),
        (ROLE_SELLER, 'Seller'),
        (ROLE_NURSERY_OWNER, 'Nursery Owner'),
        (ROLE_DELIVERY_PARTNER, 'Delivery Partner'),
        (ROLE_CONSULTANT, 'Consultant'),
        (ROLE_VENDOR, 'Vendor'),
    ]

    ROLE_CHOICES_REGISTRATION = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_EMPLOYEE, 'Employee'),
        (ROLE_CUSTOMER, 'Customer'),
        (ROLE_DOCTOR, 'Doctor'),
        (ROLE_GARDENER, 'Gardener'),
        (ROLE_SELLER, 'Seller'),
        (ROLE_NURSERY_OWNER, 'Nursery Owner'),
        (ROLE_DELIVERY_PARTNER, 'Delivery Partner'),
        (ROLE_CONSULTANT, 'Consultant'),
        (ROLE_VENDOR, 'Vendor'),
    ]

    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        _('role'),
        max_length=30,
        choices=ROLE_CHOICES,
        default=ROLE_CUSTOMER,
        help_text=_('Primary role assigned to the user.'),
    )
    phone = models.CharField(_('phone number'), max_length=20, blank=True, null=True)
    address = models.TextField(_('address'), blank=True, null=True)
    city = models.CharField(_('city'), max_length=100, blank=True, null=True)
    state = models.CharField(_('state'), max_length=100, blank=True, null=True)
    pincode = models.CharField(_('postal code'), max_length=12, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def save(self, *args, **kwargs):
        if self.role in {self.ROLE_SUPER_ADMIN, self.ROLE_ADMIN}:
            self.is_staff = True
        else:
            self.is_staff = False

        if self.role == self.ROLE_SUPER_ADMIN:
            self.is_superuser = True
        else:
            self.is_superuser = False

        super().save(*args, **kwargs)

    def get_dashboard_url(self):
        role_url_map = {
            self.ROLE_SUPER_ADMIN: 'super_admin_dashboard',
            self.ROLE_ADMIN: 'admin:index',
            self.ROLE_EMPLOYEE: 'dashboard_home',
            self.ROLE_CUSTOMER: 'customer_dashboard',
            self.ROLE_DOCTOR: 'doctor_dashboard',
            self.ROLE_GARDENER: 'gardener_dashboard',
            self.ROLE_SELLER: 'seller_dashboard',
            self.ROLE_NURSERY_OWNER: 'nursery_dashboard',
            self.ROLE_DELIVERY_PARTNER: 'delivery_dashboard',
            self.ROLE_CONSULTANT: 'consultant_dashboard',
            self.ROLE_VENDOR: 'vendor_dashboard',
        }
        return role_url_map.get(self.role, 'dashboard_home')

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    bio = models.TextField(_('bio'), blank=True, null=True)
    alternate_phone = models.CharField(_('alternate phone number'), max_length=20, blank=True, null=True)
    profile_image = models.ImageField(_('profile image'), upload_to='profiles/', blank=True, null=True)
    user_type = models.CharField(_('user type'), max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        return f"{self.user.username} Profile"


class AdminRegistrationCode(models.Model):
    code = models.CharField(_('code'), max_length=128, unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='created_admin_registration_codes',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    expires_at = models.DateTimeField(_('expires at'), blank=True, null=True)
    usage_limit = models.PositiveIntegerField(_('usage limit'), default=1)
    used_count = models.PositiveIntegerField(_('used count'), default=0)

    class Meta:
        verbose_name = _('admin registration code')
        verbose_name_plural = _('admin registration codes')
        ordering = ['-created_at']

    def clean(self):
        if self.usage_limit < 1:
            raise ValidationError({'usage_limit': _('Usage limit must be at least 1.')})
        if self.used_count > self.usage_limit:
            raise ValidationError({'used_count': _('Used count cannot exceed usage limit.')})

    @property
    def is_expired(self):
        return bool(self.expires_at and self.expires_at <= timezone.now())

    @property
    def has_uses_remaining(self):
        return self.used_count < self.usage_limit

    @property
    def can_be_used(self):
        return self.is_active and not self.is_expired and self.has_uses_remaining

    def mark_used(self):
        if not self.can_be_used:
            raise ValidationError(_('Invalid Admin Access Code'))
        self.used_count += 1
        if self.used_count >= self.usage_limit:
            self.is_active = False
        self.save(update_fields=['used_count', 'is_active'])

    def __str__(self):
        return self.code
