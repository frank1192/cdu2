from django.db import models

# Create your models here.
class Usuario(models.Model):
    Codigo = models.CharField(max_length=20, primary_key=True)  # Llave primaria: Codigo
    Identificacion = models.CharField(max_length=20)  # Identificación
    NombreApellidos = models.CharField(max_length=100)  # nombre y apellidos
    Estamento = models.CharField(max_length=50)  # Estamento
    Sexo = models.CharField(max_length=10)  # sexo
    Poblacion = models.CharField(max_length=50)  # Población
    Estado = models.CharField(max_length=50)  # estado
    Dependencia = models.CharField(max_length=100)  # dependencia

    def __str__(self):
        return self.Codigo

