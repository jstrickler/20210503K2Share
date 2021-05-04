#!/usr/bin/env python
# (c) 2017 CJ Associates
#
from django.conf.urls import url
from . import views

app_name = "words"

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^noboot', views.homenoboot, name='homenoboot'),
    url('^layout$', views.layout, name='layout'),
    url('^layoutloops$', views.layoutloops, name='layoutloops'),
    url('^cycle$', views.cycle, name='cycle'),
    url('^grid$', views.grid, name='grid'),
    url('^alerts$', views.alerts, name='alerts'),
    url('^breadcrumbs$', views.breadcrumbs, name='breadcrumbs'),
    #    url('^details/', views.food_details, name='details'),
]
