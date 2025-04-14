from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Project


# Create your views here.
@login_required
def find_all_projects(request):
    projects = list(Project.objects.all().values())

    return JsonResponse({'projects': projects})
