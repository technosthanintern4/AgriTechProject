from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    user_type = forms.ChoiceField(
        choices=UserProfile.USER_TYPES
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'user_type',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['user_type'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            'phone',
            'address',
            'city',
            'state',
            'pincode',
        ]

        widgets = {
            'phone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

            'city': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'state': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'pincode': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }