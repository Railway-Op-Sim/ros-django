from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    project_list = Project.objects.order_by('id')
    context = {'project_list': project_list}
    return render(request, 'explorer/index.html', context)

def project(request, project_id):
    project_info = Project.objects.get(id=project_id)
    context = {'project': project_info}
    return render(request, 'explorer/project.html', context)