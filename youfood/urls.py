from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.mainfun,name="mainfun"),
    path('categoryfun/<str:categoryName>',views.categoryfun,name="categoryfun"),
    path('productfun/<str:productName>',views.productfun,name="productfun"),
    path('searchfun',views.searchfun,name="searchfun"),
    path('cartshow',views.cartshow,name="cartshow"),
    path('catadd/<int:newItem>',views.cartadd,name="cartadd"),
    path('cartremove/<int:itemid>',views.cartremove,name="cartremove"),
]