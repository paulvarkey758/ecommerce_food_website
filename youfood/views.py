from django.http import request
from django.shortcuts import render
from . models import category,item

# Create your views here.
def mainfun(request):
    category_data=category.objects.all()
    return render(request,"index.html",{'catdata':category_data})

def categoryfun(request,categoryName):
    category_data=category.objects.all()
    if categoryName=="all":
        item_data=item.objects.all()
    else:
        item_data=item.objects.filter(category__name=categoryName)    
    return render(request,"category.html",{'catdata':category_data,'idata':item_data})  

def productfun(request,productName):
    category_data=category.objects.all()
    productdata=item.objects.filter(name__iexact=productName)
    return render(request,"product_details.html",{'productdata':productdata,'catdata':category_data})

def searchfun(request):
    search_query=request.GET['search']  
    print("the recieved string is",search_query)
    category_data=category.objects.all()  
    search_data=item.objects.filter(name__contains=search_query)
    return render(request,"search.html",{'searchdata':search_data,'catdata':category_data})