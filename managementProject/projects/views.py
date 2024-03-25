from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ProjectForm, TaskForm
from .models import Projects, Tasks


def index(request):
    return render(request, 'index.html')

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

def project(request, project_id):
    
    project = Projects.objects.get(PKProject=project_id)
    tasks = Tasks.objects.filter(FKProject=project_id)
    htmlTasks = []
    for task in tasks:
        taskData = {
            'id': task.id,
            'name': task.Title,
            'start': task.StartDate.strftime('%Y-%m-%d'),  # Format date as 'YYYY-MM-DD'
            'end': task.EndDate.strftime('%Y-%m-%d'),      # Format date as 'YYYY-MM-DD'
        }
        htmlTasks.append(taskData)
    print(htmlTasks)
        

    if request.method == 'GET':
        form = TaskForm()  
        return render(request, 'project.html', {'project': project, 'tasks': htmlTasks, 'form': form})
    
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # don't commit to database yet
            task.FKProject_id = project_id  # add the foreign key manually
            task.save()
            return redirect('project', project_id)
        else:
            errors = form.errors.as_data()  # Get the form errors
            return render(request, 'project.html', {'project': project, 'tasks': htmlTasks, 'form': form, 'errors': errors})

