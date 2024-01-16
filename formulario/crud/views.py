from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona

def index(request):
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')  
        # Redirigir a index.html
    else:
        form = PersonaForm()

    person = Persona.objects.all()
    
    return render(request, 'index.html', {'form': form, 'person':person})