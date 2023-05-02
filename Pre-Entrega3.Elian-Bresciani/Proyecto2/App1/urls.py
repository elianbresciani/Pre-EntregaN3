from django.urls import path
from App1 import views

urlpatterns = [
   
    path('', views.inicio, name="inicio"), #este era nuestro primer view
    path('perro', views.perroFormulario, name="perro"),
    path('dueño', views.dueñoFormulario, name="dueño"),
    path('veterinario', views.veterinarioFormulario, name="veterinario"),
    path('busquedaPerro',views.busquedaPerro,name="BusquedaPerro"),
    path('buscar/',views.buscar),
]
