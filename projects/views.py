from django.shortcuts import render
from projects.models import Project

def project_index(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'project_index.html', context)

def project_detail(request, pk):    # primary key
    context = {'project': Project.objects.get(pk=pk)}
    return render(request, 'project_detail.html', context)
