# ManagementApp

An **open-source** Software Management Software


## Installation and setup

Commands:
```
- python -m pip install Django
- django-admin startproject mysite
- python manage.py runserver
- python manage.py startapp app
- python -m pip install django-tailwind
- python -m pip install 'django-tailwind[reload]'
- python manage.py tailwind install
- python manage.py tailwind start

```

Directory structure:
```
mysite/                     
    manage.py               :command-line utility for Django project
    mysite/                 :actual Python package of the project. It's name is used to import anything inside it
        __init__.py         :empty file that makes this dir a Python package
        settings.py         :configuration for Django project
        urls.py             :URL declarations for Django project
        asgi.py             :entry-point for ASGI-compatible web servers 
        wsgi.py             :entry-point for WSGI-compatible web servers
```


## Endpoint creation
### 1) create view in the app

*root/app/views.py*
```python
def index(request):
    return HttpResponse("You're at the main page.")
```

### 2) create the url in the app

*root/app/urls.py*
```python
from . import views

urlpatterns = [
    path("", views.index)]
```

### 3) map it in the project urls

*root/project/urls.py*
```python
from projects import views

urlpatterns = [
    path("", views.index)]
```

## Database Management

1) update models.py
2) migrate to SQLite:
```
- python manage.py makemigrations
- python manage.py migrate
```