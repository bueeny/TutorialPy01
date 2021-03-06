from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone

# Create your views here.

# Class based views.
def store(request):
    context ={
        'title': 'Store',
        'products': Product.objects.all(),
    }  
    return render(request,'Nanso/store_home.html', context)

# List Based View
class ProductListView(ListView):   
    model = Product
    template_name = 'Nanso/store_home.html' # <app><modeL><view_type>.html
    context_object_name = 'products'
    dateNow = timezone.now()
    ordering = ['-productName'] #Syntax to order by which attribute

    @property
    def is_new(self):
        if (dateNow - self.date_posted) <= 100:
            return True
        else:
            return False


