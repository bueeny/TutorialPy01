from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class PostCreateView(LoginRequiredMixin, CreateView):   
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Current  login user
        return super().form_valid(form) #Save 

class PostUpdateView(UserPassesTestMixin, UpdateView):  #UserPassesTestMixin to see whether a user passes an auth test
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Current login user
        return super().form_valid(form) #Save 
    
    def test_func(self): # Checking
        post = self.get_object()
        if self.request.user == post.author: #Checking author - user
            return True
        else :
            return False

class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):  #UserPassesTestMixin to see whether a user passes an auth test
    model = Post
    success_url = '/'
    
    def test_func(self): # Checking
        post = self.get_object()
        if self.request.user == post.author: #Checking author - user
            return True
        else :
            return False
