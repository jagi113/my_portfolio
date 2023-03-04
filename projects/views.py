from django.shortcuts import render
from projects.models import Tag, Project
from projects.utils import searchProjects, paginateProjects

# Create your views here.
def index(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {"results": projects,
               "search_query": search_query,
               "custom_range": custom_range}
    return render(request, 'projects/projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, 'projects/project-detail.html', context) 