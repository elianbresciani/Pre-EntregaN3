from django.shortcuts import render
from App1.models import Dueño,Perro,Veterinario
from django.http import HttpResponse
from App1.forms import veterinarioForms,PerroForms,dueñoForms

def inicio(request):
    return render(request, 'App1/inicio.html')

def perroFormulario(request):
     if request.method == "POST":
        miFormulario = PerroForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            perro = Perro(int(informacion['id']),str(informacion['nombre']),str(informacion['raza']))
            perro.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario =PerroForms()
             
     return render(request, "App1/perroFormulario.html", {"miFormulario": miFormulario})

def veterinarioFormulario(request):
     if request.method == "POST":
        miFormulario = veterinarioForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            veterinario = Veterinario(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
            veterinario.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario =veterinarioForms()
             
     return render(request, "App1/veterinarioFormulario.html", {"miFormulario": miFormulario})

def dueñoFormulario(request):
     if request.method == "POST":
        miFormulario = dueñoForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            dueño = Dueño(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'])
            dueño.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario =dueñoForms()
             
     return render(request, "App1/dueñoFormulario.html", {"miFormulario": miFormulario})

def busquedaPerro(request):
     return render(request,'App1/busquedaPerro.html')

def buscar(request):
     if request.GET['nombre']:
          nombre = request.GET['nombre']
          perros = Perro.objects.filter(nombre__icontains=nombre)
          return render(request,'App1/resultadobusqueda.html', {"nombre":nombre, "perros":perros })
     else:
          respuesta= "No enviaste datos"

     ##return HttpResponse(respuesta)
     return render(request,"App1/inicio.html",{"respuesta":respuesta})
