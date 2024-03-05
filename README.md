# ManagementApp
An open-source Software Management Software

# Installation and setup
python -m pip install Django
django-admin startproject mysite
python manage.py runserver

mysite/                     #root directory
    manage.py               #command-line utility for this Django project
    mysite/                 #actual Python package of the project. It's name is used to import anything inside it
        __init__.py         #empty file that tells Python that this directory should be considered a Python package
        settings.py         #configuration for this Django project
        urls.py             #URL declarations for this Django project; a “table of contents” of your Django-powered site
        asgi.py             #entry-point for ASGI-compatible web servers to serve your project
        wsgi.py             #entry-point for WSGI-compatible web servers to serve your project

python manage.py startapp app

# Endpoint creation
create view in the app
create the url in the app
map it in the project urls