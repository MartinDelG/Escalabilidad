from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}" 


class InfoPago(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    cobro_total = models.IntegerField()
    cantidad_pagada = models.IntegerField()

    def __str__(self):
        return f"{self.pk}"
    

    