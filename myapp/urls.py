from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('hello/<str:user_name>', views.hello, name="hello"), #esperamos un parametro
    path('projects', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('task', views.task, name="tasks"),
    path('createNewTask', views.createNewTask, name="createNewTask"),
    path('createNewProject', views.createNewProject, name="createNewProject")
]