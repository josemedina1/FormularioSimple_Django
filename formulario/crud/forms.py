from django import forms
from crud.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['name', 'lastname', 'city', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'lastname': forms.TextInput(attrs={'class': 'input'}),
            'city': forms.TextInput(attrs={'class': 'input'}),
            'country': forms.TextInput(attrs={'class': 'input'}),
        }