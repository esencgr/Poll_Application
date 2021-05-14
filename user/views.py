from django.shortcuts import render, redirect
from .forms import RegisterForm 
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
    # form = RegisterForm(request.POST or None)

    # context = {
    #     'form' : form,
    # }
    
    # if form.is_valid():
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password')
        
    #     # database query    
    #     authenticate(username = username, password = password)

    #     if user is None 
    return render(request, "login.html")
    
def logoutUser (request):
    return render(request, "logout.html")
