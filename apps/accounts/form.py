from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=100, label='Last Name: ')
    first_name = forms.CharField(max_length=100, label='First Name: ')
    username = forms.CharField(max_length=30, label='User Name: ')
    email = forms.EmailField(max_length=200, label='E-mail: ')
    
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email',  'password1', 'password2')