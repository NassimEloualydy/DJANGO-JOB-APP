from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("pages.urls")),
    path("",include("users.urls")),
    path("",include("qualifications.urls")),
    path("",include("categoryJob.urls")) 
]   
