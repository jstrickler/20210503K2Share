"""
URL Configuration for wombats
"""
from django.urls import path
from . import views   # import views from app

app_name = "wombats"

urlpatterns = [
    # add url patterns for the wombats app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('hello', views.hello, name='hello'),
]
