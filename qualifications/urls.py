from django.shortcuts import render
from django.urls import path,include
from . import views
urlpatterns=[
path('qualifcations',views.qualifcations,name="qualifcations"),
path('submitQualification',views.submitQualification,name="submitQualification")
]