"""
Common views for the **superheroes** app



"""
from django.http import HttpResponse
from .models import Superhero

def home(request):
    """
    Main page of site

    :param request: HTTP request
    :return: HTTP Response with a message
    """
    return HttpResponse("Welcome to the superhero app")

def hero(request, hero_name):
    """
    Page with superhero and secret identity

    :param request: HTTP Request
    :param hero_name: Hero name (str)
    :return: HTTP Response with message
    """
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name)
    )

