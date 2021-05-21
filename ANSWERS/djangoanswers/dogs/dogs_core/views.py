from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .models import *

def home(request):
    return render(request, 'dogs_core/home.html', {
        'message': "Welcome to the Dogs",
        'home': True,
    })

# use generic view to handle displaying all objects
class DogListView(ListView):
    # this view uses template dog_list.html
    # use "template=..." to specify a different template
    model = Dog
    context_object_name = "dogs"

# use generic view to handle displaying a single object
# this view uses template dog_detail.html
class DogDetailView(DetailView):
    model = Dog
    context_object_name = 'dog'
    # note: could add a filter here to handle
    #  ?name=value&name=value parameters on the URL

class DogCreateView(CreateView):
    model = Dog
    fields = ['id', 'name', 'breed', 'is_neutered',
              'bites', 'weight', 'sex']


class DogListViewFancy(ListView):
    model = Dog
    context_object_name = "dogs"
    template_name = 'dogs_core/dog_list_fancy.html'


class DogDetailViewFancy(DetailView):
    """
    This view will use a template that incorporates
    the custom 'fancy' filter
    """
    model = Dog
    context_object_name = 'dog'
    template_name = 'dogs_core/dog_detail_fancy.html'


class BreedListView(ListView):
    # this view uses template breed_list.html
    model = Breed
    context_object_name = "breeds"


class BreedDetailView(DetailView):
    # this view uses template breed_detail.html
    model = Breed
    context_object_name = 'breed'

class BreedCreateView(CreateView):
    model = Breed
    fields = ['id', 'name', 'abbr']


def by_sex(request, sex):
    """
    Request a list of dogs by sex
    :param sex: 'm' or 'f'
    the sex parameter is part of the url
     for example:
      .../by_sex/m

    the name parameter is a GET request parameter
    which comes after the ? in the URL
    for example:
      .../by_sex/f/n
    """

    # check GET parameter from URL (after '?' in URL)
    name = request.GET.get('name')

    # add query for sex
    queries = [Q(sex=sex)]

    # if ?name=xxx is supplied on URL,
    # add name query
    if name:
        queries.append(Q(name__istartswith=name))

    # filter dogs with optional name query
    dogs = Dog.objects.filter(*queries)
    return render(request, 'dogs_core/dog_list.html', {
        'dogs': dogs,
    })

def shortest(request):
    """
    Return the shortest dog name in the db.

    This uses an aggregate method on a custom manager
    (see dogs_core.models)

    :param request: HTTP request
    :return: HTML page
    """
    shortest_name = Dog.objects.shortest_name()
    return render(request, 'dogs_core/shortest.html', {
        'shortest_name': shortest_name,
    })

def dogs_include(request):
    """
    Use template containing {% include ... %} directive
    """
    dogs = Dog.objects.all()
    return render(request, 'dogs_core/dogs_include.html', {
        'dogs': dogs,
    })
