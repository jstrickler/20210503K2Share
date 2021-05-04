"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('heroformset', views.heroformset, name='heroformset'),
]

