from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="Home"),
    path('login',views.login,name="login"),
    path('signin',views.signin,name="signin"),

]