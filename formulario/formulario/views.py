from django.shortcuts import render
from .forms import TuFormulario

def index(request):
    if request.method == 'POST':
        formulario = TuFormulario(request.POST)
        if formulario.is_valid():
            valor_input = formulario.cleaned_data['tu_input']
            return render(request, 'index.html', {'valor_input': valor_input})
    else:
        formulario = TuFormulario()

    return render(request, 'index.html', {'formulario': formulario})
