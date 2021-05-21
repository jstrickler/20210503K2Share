"""
URL Configuration for dogs_core
"""
from django.urls import path, include
from . import views

app_name = 'dogs_core'

urlpatterns = [
    # routes for web pages (not API)

    # home page
    path('', views.home, name="home"),

    # list all objects
    path('dogs', views.DogListView.as_view(), name="dogs"),
    path('breeds', views.BreedListView.as_view(), name="breeds"),

    # list details for an object
    path('dog/<str:pk>', views.DogDetailView.as_view(), name="dog"),

    path('breed/<str:pk>', views.BreedDetailView.as_view(), name="breed"),

    # list dogs by sex (and optional name)
    path('by_sex/<str:sex>', views.by_sex, name="by_sex"),

    # get shortest name
    path('shortest', views.shortest, name='shortest'),

    # alternate dog list using template with 'fancy' filter
    path('fancy_list', views.DogListViewFancy.as_view(), name='fancy_list'),

    # use the "fancy" view and template that uses a
    # custom filter
    path(
        'fancy_detail/<str:pk>',
        views.DogDetailViewFancy.as_view(),
        name='fancy_detail'
    ),

    path('dogs_include', views.dogs_include, name='dogs_include'),

    # routes for the API (delegated to dogs_core.api.urls)

    path('api/', include('dogs_core.api.urls', namespace="api")),
]
