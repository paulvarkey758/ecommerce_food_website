from django.shortcuts import render
from django.http import HttpResponse
from . models import fooddata

# Create your views here.
def mainfun(request):
    data=fooddata.objects.all()
    return render(request,"home.html",{'datas':data})

def itemfun(request):
    return render(request,"itempage.html")
