from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the main page.")

def projects(request):
    return HttpResponse("You're seeing your projects.")

def project(request,order):
    return HttpResponse("You're seeing project "+str(order))