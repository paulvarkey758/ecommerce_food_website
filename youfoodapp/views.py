from django.shortcuts import render
from django.http import HttpResponse
from . models import fooddata

# Create your views here.
def mainfun(request):
    data=fooddata.objects.all()
    return render(request,"home.html",{'datas':data})
    

def itemfun(request,name):
    product=fooddata.objects.get(name=name)
    return render(request,"itempage.html",{'products':product})
   
def categoryfun(request,catname):
    cat=fooddata.objects.filter(category__iexact=catname)
    data=fooddata.objects.all()
    if catname=='all':
        return render(request,"home.html",{'datas':data})
    else:
        return render(request,"category.html",{'catdata':cat})


def searchfun(request):
    key=request.GET.get('searchkey')
    result=fooddata.objects.filter(name__icontains=key)
    return render(request,"searchtab.html",{'result':result,'key':key})

    
    
        
