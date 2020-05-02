from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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
def home(request):
    context ={
        'title': 'Home',
        'posts': Post.objects.all()
    }  
    return render(request,'App01/home.html', context)

def about(request):
    return render(request,'App01/about.html', {'title':'About'})