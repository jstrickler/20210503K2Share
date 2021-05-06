"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views   # import views from app

app_name = "superheroes"

urlpatterns = [
    path('', views.home, name='home'),
    path('context', views.context, name='context'),
    path('request_dump', views.request_dump, name='request_dump'),
]
