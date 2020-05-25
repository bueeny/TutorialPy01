from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name = 'App01-home'), #class based view leave as hompepage
    path('Nanso/store', views.store, name = 'store-home'), 
]   