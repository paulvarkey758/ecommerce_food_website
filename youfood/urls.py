from django.urls import path
from . import views
urlpatterns=[
    path('',views.mainfun,name="mainfun"),
    path('categoryfun/<str:categoryName>',views.categoryfun,name="categoryfun"),
    path('productfun/<str:productName>',views.productfun,name="productfun"),
    path('searchfun',views.searchfun,name="searchfun"),
]