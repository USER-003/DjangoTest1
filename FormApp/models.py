from django.db import models

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10) 
    altura = models.FloatField()
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre
