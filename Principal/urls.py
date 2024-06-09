
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='inicio'),
    path('IniciarSesion/',views.InicioSesion, name= 'iniSesion'),
    path('RegistroEstudiante/',views.regisEstudiante, name ='Esturegistro'),
    path('RegistroProfesor/',views.regisProfesor, name= 'reprofesor'), #se usa name para la direccion en html
    path('RegistroExi/',views.registroEs, name= 'unRegistro'), 
    path('Prueba/',views.prueba), 

]

