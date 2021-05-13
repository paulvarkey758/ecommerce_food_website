from django.urls import path
from . import views

urlpatterns=[
    path('',views.mainfun,name="mainfun"),
    path('itemfun/<str:name>',views.itemfun,name="itemfun"),
    path('category/<str:catname>',views.categoryfun,name='categoryfun'),
    path('searchpage',views.searchfun,name="searchfun"),
]
