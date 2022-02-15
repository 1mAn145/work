from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login as login_form , logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from apps.accounts.models import UserProfile
from apps.accounts.form import SignUpForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_form(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Login Error! Username or Password is incorrect')
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login_form(request, user)
            # create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            # data.image = 'users/user.jpg'
            data.save()
            messages.success(request, 'Success sign up')
            return HttpResponseRedirect('/')
        else:
            messages.info(request, form.errors)
            return HttpResponseRedirect('#')
        return redirect('/')
   
    return render(request, 'register.html')


def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')



