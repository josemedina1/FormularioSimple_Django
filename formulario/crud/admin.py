from django.contrib import admin
from .models import Persona

"""
    Esta clase permite personalizar la apariencia 
    y el comportamiento del modelo Persona en el panel de administración.
    la clase PersonaAdmin permite especificar qué campos se deben mostrar 
    y cómo se deben mostrar en la lista de objetos.
"""

class PersonaAdmin(admin.ModelAdmin):
    # Especifica los campos del modelo que se mostrarán 
    # en la lista de objetos en la interfaz de administración
    list_display = 'name', 'lastname', 'city', 'country'
    
# Registra el modelo Persona 
admin.site.register(Persona,PersonaAdmin)