from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserProfileForm
 
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_name.is_valid():
            form.save()
            user = form.save()
            profile =  profile_form.save(commit = False) #Don't save to database yet
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You are now able to login.') #message
            return redirect('login') # redirect back home
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'users/register.html',context) #context = 'form' = for,



@ login_required # To add in login authentication to access this login route
def profile(request):
    return render(request, 'users/profile.html')