from django.urls import path
from . import views

urlpatterns=[
    path('',views.mainfun,name="mainfun"),
    path('itemfun',views.itemfun,name="itemfun"),
]
