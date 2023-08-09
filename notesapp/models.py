from django.db import models

# Create your models here.

"""seleccionas todo lo que se quiere comentar ctrl+}"""
# class Tasks(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60)
#     desc = models.CharField(max_length=255)



class Regist(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=150, unique=True)
    
    class Meta:
        db_table : 'Regist'


class tarea(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=30, null=True)
    titulo = models.CharField(max_length=60)
    nota= models.CharField(max_length=350)
    ceccion = models.CharField(max_length=40)
    link  = models.CharField(max_length=400,null=True)

    class Meta:
        db_table : 'tarea'
