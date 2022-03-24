from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('urlForm/', views.urlForm, name='urlForm'),
    path('urlRedir/', views.redirection, name='urlRedir'),
]
