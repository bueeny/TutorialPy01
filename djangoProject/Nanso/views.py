from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

# Class based views.
def store(request):
    context ={
        'title': 'Store',
    }  
    return render(request,'Nanso/store_home.html', context)
