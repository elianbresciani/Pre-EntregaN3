from django.db import models

# Create your models here.

class Perro(models.Model):
    raza= models.CharField(max_length=30)

    nombre= models.CharField(max_length=40)

    

 

class Dueño(models.Model):

    nombre= models.CharField(max_length=30)

    apellido= models.CharField(max_length=30)

    email= models.EmailField()

 

class Veterinario(models.Model):

    nombre = models.CharField(max_length=30)

    apellido= models.CharField(max_length=30)

    email= models.EmailField()

    profesion= models.CharField(max_length=30)

 
