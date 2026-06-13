from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation

        fields = [
            'appointment_date'
        ]

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
        }