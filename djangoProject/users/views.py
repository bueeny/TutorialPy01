from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,UserProfileForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # profile_form.instance.user = user
            # profile_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You are now able to login.') #message
            return redirect('login') # redirect back home
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html',context) #context = 'form' = for,

@login_required # To add in login authentication to access this login route
def profile(request): # To fill in form with existing data

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance = request.user.profile)

        if user_update_form.is_valid() and profile_form.is_valid():
            user_update_form.save()
            profile_form.save()
            username = user_update_form.cleaned_data.get('username')
            messages.success(request, f'Profile has been updated successfully for {username}') #message
            return redirect('profile')

    else:
        user_update_form = UserUpdateForm(instance = request.user)
        profile_form = UserProfileForm(instance = request.user.profile)

    # create a context
    context = {'user_update_form':user_update_form,'profile_form': profile_form }

    return render(request, 'users/profile.html', context)