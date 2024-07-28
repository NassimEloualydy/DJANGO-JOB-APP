from . import views
from django.urls import path,include

urlpatterns=[
    path('category/',views.category,name="Category"),
    path("addCategory/",views.addCategory,name="addCategory")
]