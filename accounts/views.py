from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.
def registerfun(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username is already taken!")
            return redirect('registerfun')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email is already taken!")
            return redirect('registerfun')
        elif  password1!=password2:
            messages.info(request,"Passwords are not match!")
            return redirect('registerfun')
        else:    
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            print("user created successfully")
            return redirect('/')
    else:    
        return render(request,"registration.html")


def loginfun(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('loginfun')
    else:
        return render(request,"login.html")


def logoutfun(request):
    auth.logout(request)
    return redirect('/')                    