from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate     
from django.contrib import messages

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        newUser = User(username = username)
        newUser.set_password(password)      # encrypted

        newUser.save()
        login(request,newUser)
        messages.success(request,"Registration Successful..")
        return redirect("home")

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

        if user is None:
            messages.info(request,"Username or password is incorrect.Try again.")
            return render(request, "login.html", context)
        
        messages.success(request,"Login Successful..")
        login(request,user)
        return redirect("home")
    
    return render(request, "login.html", context)

def logoutUser (request):
    return render(request, "logout.html")
