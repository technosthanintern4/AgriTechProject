from django import forms
from .models import GardenerBooking


class GardenerBookingForm(forms.ModelForm):

    class Meta:
        model = GardenerBooking

        fields = [
            'service_type',
            'booking_date',
            'address',
            'notes'
        ]

        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }