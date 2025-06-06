from django.db import models

# Create your models here.
class Project(models.Model): #creamos una tabla 
    name = models.CharField(max_length=200) #creamos los campos
    
    def __str__(self):
        return self.name #mostramos los nombres de los proyectos en el admin

class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name