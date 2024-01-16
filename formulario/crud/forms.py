from django import forms
from crud.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['name', 'lastname', 'city', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inputform'}),
            'lastname': forms.TextInput(attrs={'class': 'inputform'}),
            'city': forms.TextInput(attrs={'class': 'inputform'}),
            'country': forms.TextInput(attrs={'class': 'inputform'}),
        }