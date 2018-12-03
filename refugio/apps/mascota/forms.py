from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',
        }

        SEXO = (
            ('Macho', 'Macho'),
            ('Hembra', 'Hembra'),
        )


        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}, choices=SEXO), 
            'edad_aproximada': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'DD/MM/AAAA'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
