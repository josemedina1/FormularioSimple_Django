from django import forms
from formconnect.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['name', 'lastname', 'city', 'country']