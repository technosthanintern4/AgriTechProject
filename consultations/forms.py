from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation

        fields = [
            'appointment_date',
            'animal_type',
            'animal_name',
            'description',
            'area_size',
            'duration',
        ]

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'animal_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g., Dog, Cat, Goat, Cow'
                }
            ),
            'animal_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name of the pet/animal'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Describe your issue or service requirement in detail'
                }
            ),
            'area_size': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g., 1000 sqft, 5 acres'
                }
            ),
            'duration': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g., 3 months, 1 year'
                }
            ),
        }