from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Prueba

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1> LISTA DE FAMILIARES</h1/>')


def un_template(request):
    # template = loader.get_template('index.html')
    
    prueba1 = Prueba(nombre='Josefina', edad= 32)
    prueba2 = Prueba(nombre='Rene', edad=88)
    prueba3 = Prueba(nombre='Marcos', edad=22)
    prueba1.save()
    prueba2.save()
    prueba3.save()
    # render = template.render({'listado_familiares': [prueba1, prueba2, prueba3]})
    # return HttpResponse(render)

    return render(request, 'index.html', {'listado_familiares': [prueba1, prueba2, prueba3]} )

def listado_familiares(request):
    
    template = loader.get_template('index.html')
    
    lista_familiares = Prueba.objects.all()
    
    render = template.render({'lista_familiares': lista_familiares})
    
    return HttpResponse(render)

    