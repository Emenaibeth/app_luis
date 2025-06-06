from django.shortcuts import render, redirect
from django.http import HttpResponse #devuelve msj al navegador
from django.http import JsonResponse #devuelve un conjunto de datos JSON
from .models import Project, Task #importamos desde model, la clase project
from django.shortcuts import get_object_or_404 #si un objeto no  existe, devuelve una pagina 404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    #return HttpResponse("Index Page") para retornar string
    title = "Curso Django APP Tareas!!"
    return render(request, 'index.html', {'title': title}) #renderizamos un archivo html

def about(request):
    username = "Luis"
    return render(request, 'about.html', {'username': username})

def hello(request, user_name):
    return HttpResponse("<h1>HELLO %s </h1>" % user_name)


def projects(request):
    #projects = list(Project.objects.values()) #convertimos a lista
    #return JsonResponse(projects, safe=False)
    projects = Project.objects.values()
    return render(request, 'projects/project.html', {'projects':projects})

#pasando parametros
"""def task(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id) #es lo mismo que el anterior, solo que sino existe, arroja un 404
    #return HttpResponse('task: %s' % task.title)
    return render(request, 'task.html', {'task': task})
    """

def task(request):
    task = Task.objects.values()
    return render(request, 'tasks/task.html', {'task': task})

def createNewTask(request):
    #si es metodo GET renderizamos la vista, ya que GET solicita al servidor
    if request.method == 'GET':
         return render(request, 'tasks/createNewTask.html', {
         'form' : CreateNewTask() #me crea el formulario
        })
    else:
        #si es metodo POST, se reciben los datos, ya que POST envia datos al servidor
        Task.objects.create(title=request.POST['title'], descripcion=request.POST['descripcion'], project_id=1)
        return redirect('tasks') #se cambia de pagina, nos redirecciona

def createNewProject(request):
    if request.method == 'GET':
          return render(request, 'projects/createProjects.html', {
          'form': CreateNewProject()
         })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks' : tasks
    })
