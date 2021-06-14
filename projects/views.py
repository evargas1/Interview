from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    url = str(Project.image).replace('static', '')
    context = {
        'projects': projects, 
        'url': url,
    }
    return render(request, 'index.html', context)
# this function is grabing information from the database and making it possible for you to see
