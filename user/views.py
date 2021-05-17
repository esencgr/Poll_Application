from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages, auth

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if User.objects.filter(username = username).exists():
            messages.info(request,"User name is already exists ")
            return redirect("register") 
        else:
            newUser = User(username = username)
            newUser.set_password(password)      # encrypted
            newUser.save()
            login(request,newUser)
            messages.success(request,"Registration Successful..")
            return redirect("login")

    context = {
        'form' : form,
    }
    return render(request, "register.html", context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        'form' : form,
    } 

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')  

        # database query    
        user = authenticate(username = username, password = password) 

        if user is not None:
            auth.login(request,  user)
            messages.success(request,"Login Successful..")
            return redirect("home")

        else:
            messages.info(request,"Username or password is incorrect.Try again.")
            return render(request, "login.html", context)

    return render(request, "login.html", context)


def logoutUser ( request):
    logout(request)
    messages.success(request,"Logout Successful..")
    return redirect("login")