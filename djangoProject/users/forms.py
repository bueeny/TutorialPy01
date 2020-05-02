from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField(min_value = 0,max_value = 99)


    class Meta:
        model = User
        fields = ['username','email','age','password1','password2']
