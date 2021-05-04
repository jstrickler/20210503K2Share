from django.urls import path
from . import views

app_name = 'greet'

urlpatterns = [
    path('', views.home, name="home"),
]

