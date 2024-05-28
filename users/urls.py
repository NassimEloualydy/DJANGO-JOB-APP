from django.shortcuts import render
from django.urls import path,include
from . import views
# Create your views here.
urlpatterns=[
path('signinUser',views.signinUser,name="signinUser"),
path('loginUser',views.loginUser,name="loginUser"),
path("logout",views.logout,name="logout")
]