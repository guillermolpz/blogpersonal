from django.shortcuts import render, HttpResponse
#Modelos
from .models import Project
# Create your views here.
def perfil(request):
    projects = Project.objects.all()
    return render(request, 'perfil.html', {'projects':projects})
    #project1 = Project(titulo="Projecto 1", descripcion="Descripcion 1")
    #project1.save()
    #project2 = Project(titulo="Projecto 2", descripcion="Descripcion 2")
    #project2.save()
    #project3 = Project(titulo="Projecto 3", descripcion="Descripcion 3")
    #project3.save()
    
    #projects = Project.objects.all()
    
    #return HttpResponse(projects)