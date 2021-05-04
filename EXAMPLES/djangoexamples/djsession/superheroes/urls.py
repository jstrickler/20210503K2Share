"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views   # import views from app



urlpatterns = [
    path('', views.home, name='home'),
    path('hero/<str:hero_name>/', views.hero, name="hero"),
]

