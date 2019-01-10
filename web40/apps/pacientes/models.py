from django.db import models

# Create your models here.

class Paciente(models.Model):
    Apellido= models.CharField(max_length=30)
    Nombre = models.CharField(max_length=30)
    DNI = models.IntegerField()
    FechaNacimiento= models.DateField()
    SEXO = (('F', 'Femenino'),('M','Masculino'))
    Sexo = models.CharField(max_length= 1, choices= SEXO)

    def NombreCompleto(self):
        cadena= "{0}, {1}"
        return cadena.format(self.Apellido, self.Nombre)

    def __str__(self):
        return self.NombreCompleto()
