from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .formulario import CrearEstudiante

from django.shortcuts import render, redirect

from .models import Estudiante

# Create your views here.
def index(request):
    return render(request, 'index.html')


def InicioSesion(request):
    return  render(request, 'IniciarSesion.html')


#Funcion para registrar un estudiante en lal base de datos
def regisEstudiante(request):
    if request.method == 'POST':
        primer_nombre = request.POST.get('primerNombre')
        primer_Apellido = request.POST.get('primerApellido')
        Genero = request.POST.get('genero')
        fecha_N = request.POST.get('fechaNacimiento')
        telefono = request.POST.get('telefono')
        nivel_E = request.POST.get('nivelEscolar')
        contraseña = request.POST.get('password')


        segundo_nombre = request.POST.get('segundoNombre')
        segundo_Apellido = request.POST.get('segundoApellido')
        nacionalidad = request.POST.get('nacionalidad')
        edad = request.POST.get('edad')
        direccion = request.POST.get('direccion')
        correo = request.POST.get('correo')

        # Crea una instancia del modelo Estudiante y guarda en la base de datos
        estudiante = Estudiante(
            primerNombre=primer_nombre,  #campo base de datos y variable con los datos del name del formulario
            segundoNombre=segundo_nombre,
            primerApellido=primer_Apellido,
            segundoApellido=segundo_Apellido,
            genero=Genero,
            nacionalidad=nacionalidad,
            fechaNacimiento=fecha_N,
            edad=edad,
            telefono=telefono,
            direccion=direccion,
            nivelEscolar=nivel_E,
            correo=correo,
            password=contraseña,
            # Completa los otros campos aquí
        )
        estudiante.save()

        # Si se registra existosamente nos envia a esta url que trae una funcion HTTps
        return redirect('unRegistro')
    #Si no entra el if nos recarga la pagina
    return render(request, 'registroEstudiante.html')


# def regisEstudiante(request):
  #  return  render(request, 'registroEstudiante.html', {
   #     'formulario': CrearEstudiante()
    #})



def regisProfesor(request):
    return  render(request, 'registroProfesor.html')


def registroEs(request):
    return HttpResponse('Estudiante correctamente registrado')


def prueba(request):
    return  render(request, 'prueba.html')
