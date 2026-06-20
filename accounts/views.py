from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect

from .forms import RegisterForm, UserProfileForm
from .models import AdminRegistrationCode, UserProfile
from .roles import get_role_dashboard_redirect, assign_user_to_role_group

from orders.models import Order
from consultations.models import Consultation
from gardeners.models import GardenerBooking
from wishlist.models import Wishlist


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save(commit=False)
                    admin_code = None

                    if user.role == user.ROLE_ADMIN:
                        code_value = form.cleaned_data.get('admin_access_code')
                        admin_code = (
                            AdminRegistrationCode.objects
                            .select_for_update()
                            .filter(code=code_value)
                            .first()
                        )
                        if not admin_code or not admin_code.can_be_used:
                            raise ValidationError('Invalid Admin Access Code')

                    user.save()
                    UserProfile.objects.get_or_create(user=user)
                    assign_user_to_role_group(user)

                    if admin_code:
                        admin_code.mark_used()

                login(request, user)
                if user.role == user.ROLE_ADMIN:
                    messages.success(request, 'Admin account created successfully.')
                return redirect(get_role_dashboard_redirect(user))
            except ValidationError:
                form.add_error('admin_access_code', 'Invalid Admin Access Code')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(get_role_dashboard_redirect(user))
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    consultations = Consultation.objects.filter(user=request.user).order_by('-created_at')
    bookings = GardenerBooking.objects.filter(user=request.user).order_by('-created_at')
    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(request, 'accounts/dashboard.html', {
        'orders': orders,
        'consultations': consultations,
        'bookings': bookings,
        'wishlist_items': wishlist_items,
    })


@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form})
