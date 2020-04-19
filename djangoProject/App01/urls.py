from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'App01-home'), #leave as hompepage
    path('about/', views.about, name = 'App01-about') 
]   