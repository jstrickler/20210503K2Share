"""
URL Configuration for apiv1
"""
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views   # import views from app

schema_view = get_swagger_view(title='Superhero API')

urlpatterns = [
    # add url patterns for the apiv1 app here

    # Example:
    path('schema', schema_view, name='schema'),
    path('herolist', views.superhero_list, name='superherolist'),
    path('hero/<int:pk>', views.superhero_detail, name='superherodetail'),
    path('enemylist', views.EnemyList.as_view(), name='enemylist'),
    path('enemy/<int:pk>', views.EnemyDetail.as_view(), name='enemydetail'),
]
