from django import forms

#esto se le envia al html y lo convierte en input
class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=200)
    descripcion = forms.CharField(label="Descripción de tarea", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)