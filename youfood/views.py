from django.http import request
from django.shortcuts import redirect, render
from . models import cart, category,item
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="loginfun")
def cartshow(request):
    current_user=request.user.id    
    cart_products=item.objects.filter(cart__cartuser=current_user)
    cart_total=0
    for i in cart_products:
        cart_total+=i.price
    return render(request,"cart.html",{'cp':cart_products,'total':cart_total})
@login_required(login_url="loginfun")
def cartadd(request,newItem):
    current_user=request.user
    current_item=item.objects.get(id=newItem)
    cartusers=cart.objects.all()
    user_status=False
    for i in cartusers:
        if i.cartuser.id==current_user.id:
            user_status=True
            break
    if user_status==True:        
        cartObj=cart.objects.get(cartuser=current_user)
        cartObj.item.add(current_item)
    else:    
        cartObj=cart(cartuser=current_user)
        cartObj.save()
        cartObj.item.add(current_item)
    return redirect('cartshow')

def cartremove(request,itemid):
        current_user=request.user
        current_item=item.objects.get(id=itemid)
        cartObj=cart.objects.get(cartuser=current_user)
        cartObj.item.remove(current_item)
        return redirect('cartshow')