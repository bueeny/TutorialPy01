from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'App01-home'),
    path('about/', views.about, name = 'App01-about') #leave as hompepage
]   