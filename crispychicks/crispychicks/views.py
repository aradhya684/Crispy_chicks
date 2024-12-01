
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,logout,login
from products.models import Product

def home(request):
    return render(request,"home.html")


def user_login(request):
    
    if request.method == 'GET':
        return render(request,"login.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_auth = authenticate(username = username,password = password)
        if user_auth is not None:
            login(request,user_auth)
            print(request.user.first_name)
            return HttpResponseRedirect('/menu')
        else:
            return render(request,"login.html",{"message":"Login Failed"})

def register(request):
    if request.method=="GET":
        # form = UserCreationForm()
        form = CustomUserCreationForm 
        return render(request,"register.html",{"form":form})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")





