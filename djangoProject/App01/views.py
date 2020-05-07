from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

## Dummy data
# posts = [
#     {
#         'author':'RandomGuy',
#         'title': 'Blog Post 1',
#         'content': 'Hiiii',
#         'date_posted': 'August 1 2019'
#     },
    
#     {
#         'author':'Walter',
#         'title': 'Blog Post 2',
#         'content': 'Welcome!',
#         'date_posted': 'August 4 2019'
#     },
# ]


# Create your views here.

# Class based views.
def home(request):
    context ={
        'title': 'Home',
        'posts': Post.objects.all()
    }  
    return render(request,'App01/home.html', context)

def about(request):
    return render(request,'App01/about.html', {'title':'About'})


# List Based View
class PostListView(ListView):   
    model = Post
    template_name = 'App01/home.html' # <app><modeL><view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #Syntax to order by which attribute

class PostDetailView(DetailView):   
    model = Post