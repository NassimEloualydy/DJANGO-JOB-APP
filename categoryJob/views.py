from django.shortcuts import render
from django.http import JsonResponse
from qualifications.models import Qualifications
from django.db import connection

# Create your views here.
def category(request):
    return render(request,"category.html")
def addCategory(request):
    if request.session.get('first_name',None) is not None:
        name=request.post["name"]
        description=request.post["description"]
        print('name')
    else:
        return JsonResponse({
            "type":"Warning",
            "message":"Unuathorized Request !!"
        })
    return
