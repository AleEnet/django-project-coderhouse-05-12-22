from django.db import models

class Familiares (models.Model):
    Nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 450)
    Edad = models.IntegerField()
    image = models.ImageField(upload_to="familiares/images")
    
