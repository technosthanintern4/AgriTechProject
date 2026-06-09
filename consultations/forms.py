from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation

        fields = [
            'plant_name',
            'disease_description',
            'plant_image',
            'appointment_date'
        ]

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'plant_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'disease_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),
        }