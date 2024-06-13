from django.shortcuts import render
from django.urls import path,include
from . import views
urlpatterns=[
path('qualifcations',views.qualifcations,name="qualifcations"),
path('submitQualification',views.submitQualification,name="submitQualification"),
path("getDataQualifications",views.getDataQualifications,name="getDataQualifications"),
path("deleteQualifications",views.deleteQualifications,name="deleteQualifications")
]