from django.db import models

# Create your models here.
class Registro(models.Model):

    OPCIONES_GENERO = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ]

    OPCIONES_NACIONALIDAD = [
        ('Dominicana', 'Dominicana'),
        ('Haitiana', 'Haitiana'),
        ('Venezolana', 'Venezolana'),
        ('Colombiana', 'Colombiana'),
        ('Peruana', 'Peruana'),
    ]

    OPCIONES_CURSO = [
        ('1ro de bachillerato', '1ro de bachillerato'),
        ('2do de bachillerato', '2do de bachillerato'),
        ('3ro de bachillerato', '3ro de bachillerato'),
        ('4to de bachillerato', '4to de bachillerato'),
        ('5to de bachillerato', '5to de bachillerato'),
        ('6to de bachillerato', '6to de bachillerato'),
    ]

    nombre = models.CharField(max_length=100, null=True, blank=True)  
    apellido = models.CharField(max_length=100, null=True, blank=True)  
    fecha = models.CharField(max_length=100, null=True, blank=True)  
    genero = models.CharField(max_length=15, choices=OPCIONES_GENERO, null=True, blank=True)  
    nacionalidad = models.CharField(max_length=100, choices=OPCIONES_NACIONALIDAD, default="Dominicana", null=True, blank=True)  
    direccion = models.CharField(max_length=100, null=True, blank=True) 
    contacto = models.CharField(max_length=15, null=True, blank=True)
    matricula = models.CharField(max_length=50, null=True, blank=True)
    curso = models.CharField(max_length=50, choices=OPCIONES_CURSO, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"