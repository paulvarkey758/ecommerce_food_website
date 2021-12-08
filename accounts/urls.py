from django.urls import path
from . import views

urlpatterns=[
    path('register',views.registerfun,name="registerfun"),
    path('login',views.loginfun,name="loginfun"),
    path('logout',views.logoutfun,name="logoutfun"),
]