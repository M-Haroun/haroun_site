from django.shortcuts import render,get_object_or_404
from .models import Project

# Create your views here.
def projects(request):
    search=Project.objects.all()
    context={
        'projects':search
    }
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    project = get_object_or_404(Project,pk=pk)
    project_imgs = project.images.all()
    context = {'project':project,
               'imgs':project_imgs
               }
    return render(request, 'projects/project.html',context)