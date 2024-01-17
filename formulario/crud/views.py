from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

def index(request):
    error_message = None

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            # Validar si está vacio el formulario
            '''
                form.cleaned_data['nombre_input']
                se obtiene el valor del campo por ejemplo 'name' del formulario
                después devalidar "form.is_valid()". 
            '''
            if not form.cleaned_data['name'] and not form.cleaned_data['lastname'] and not form.cleaned_data['city'] and not form.cleaned_data['country']:
                # El formulario está vacío, realiza alguna acción (por ejemplo, muestra un mensaje de error)
                error_message = "El formulario está vacío. Todos los campos son obligatorios."
            else:
                # Guardar los datos en la base de datos u otras acciones necesarias
                form.save()
                return redirect('index')
    else:
        form = PersonaForm()

    person = Persona.objects.all()

    return render(request, 'index.html', {'form': form, 'person': person, 'error_message': error_message})
