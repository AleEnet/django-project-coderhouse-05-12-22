from django.db import models

class Familiare (models.Model):
    Familiar = models.CharField(max_length= 50) 
    Nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    Edad = models.IntegerField()
    image = models.ImageField(upload_to="familiares/images")
    
