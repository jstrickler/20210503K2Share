from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Main page of site

    :param request: HTTP request
    :return: HTTP Response with a message
    """
    return HttpResponse("Welcome to the superhero app")

def context(request):
    data = {'message': "Using a context processor"}
    return render(request, 'superheroes/context.html', data)

def request_dump(request):
    data = {'message': "Dumping the request object"}
    return render(request, 'superheroes/request_dump.html', data)

