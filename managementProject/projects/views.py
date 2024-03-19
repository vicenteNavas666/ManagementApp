from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ProjectForm
from .models import Projects


def index(request):
    return HttpResponse('You are at the main page.')

def projects(request):

    if request.method == 'GET':
        projects = Projects.objects.all()  # Fetch all existing projects
        form = ProjectForm()  # Initialize the form
        return render(request, 'projects.html', {'projects': projects, 'form': form})

    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()                                                                                 #validation, instantiation and insertion is all automatic based on forms.py and models.py
            return redirect('projects')                                                                 #redirect to the same page to display updated projects
        else:                                                                                           #form is not valid, re-render the page with the form and existing projects
            return render(request, 'projects.html', {'error': "form error"})