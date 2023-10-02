from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django .http import HttpResponse
from django .contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate



# Create your views here.
def log(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('log')
    return render(request,'log.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first name']
        email=request.POST['email']
        password=request.POST['password']
        conpassword=request.POST['password2']
        if password==conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect ("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
        
            else:


                user=User.objects.create_user(username=username,password=password,email=email)
                user.save() 
                return redirect('log')
        else:
            messages.info(request,'password not matching')
            return redirect("register")
        return redirect('/')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')    