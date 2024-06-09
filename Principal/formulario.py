from django import forms

class CrearEstudiante(forms.Form):
    primerNombre = forms.CharField(label="Primer Nombre",max_length=50)
    primerApellido = forms.CharField(label= "Primer Apellido", max_length=50)
    genero = forms.CharField(label= "Genero", max_length=50)
    fechaNacimiento = forms.DateField(label="Fecha Nacimiento")
    telefono = forms.CharField(label= "Telefono", max_length=50)
    nivelEscolar = forms.CharField(label= "Nivel de Escolaridad", max_length=50)
    password = forms.CharField(label= "Contraseña", max_length=50)


    segundoNombre = forms.CharField(label="Segundo Nombre",max_length=50)
    segundoApellido = forms.CharField(label="Segundo Apellido",max_length=50)
    nacionalidad = forms.CharField(label="Nacionalidad",max_length=50)
    edad = forms.CharField(label="Edad",max_length=50)
    direccion = forms.CharField(label="Direccion",max_length=50)
    correo = forms.CharField(label="Correo",max_length=50)
    