from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AdminRegistrationCode, UserProfile


User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES_REGISTRATION,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    admin_access_code = forms.CharField(
        required=False,
        label='Admin Access Code',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'Enter Admin Access Code',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'admin_access_code', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        code = (cleaned_data.get('admin_access_code') or '').strip()

        if role != User.ROLE_ADMIN:
            cleaned_data['admin_access_code'] = ''
            return cleaned_data

        if not code:
            self.add_error('admin_access_code', 'Invalid Admin Access Code')
            return cleaned_data

        admin_code = AdminRegistrationCode.objects.filter(code=code).first()
        if not admin_code or not admin_code.can_be_used:
            self.add_error('admin_access_code', 'Invalid Admin Access Code')
            return cleaned_data

        cleaned_data['admin_access_code'] = code
        return cleaned_data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone', 'address', 'city', 'state', 'pincode', 'is_active']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'alternate_phone', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'alternate_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
