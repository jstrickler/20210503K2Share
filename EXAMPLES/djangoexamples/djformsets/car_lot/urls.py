"""
URL Configuration for car_lot
"""
from django.urls import path
from . import views   # import views from app

app_name = "car_lot"

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.CarListView.as_view(), name='list'),
    path('add', views.CarAddView.as_view(), name='add'),
    # add url patterns for the car_lot app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
