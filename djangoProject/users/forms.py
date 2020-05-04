from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
                                                          
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['username','email']

# # Use html 5 built-in date input
# class DateInput(forms.DateInput):
#     input_type = 'date'

class UserProfileForm(ModelForm):
    class Meta: 
        model = Profile 
        fields = ['image','birthday','bio','location']
        # widgets = {'birthday': DateInput(format = '%Y-%m-%d',attrs = {'placeholder': 'Insert Birth Date Here'})}
        widgets = {'birthday': forms.DateInput( attrs={'class':'form-control', 'placeholder':'Select your birthdate', 'type':'date'})}



