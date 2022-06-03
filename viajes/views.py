from django.shortcuts import render
from viajes.models import Viaje

# Create your views here.
def listar_viajes(request):
    lista_viajes=Viaje.objects.all() 
    context= {'lista_viajes':lista_viajes}
    return render(request, 'lista_viaje.html', context=context)
    
