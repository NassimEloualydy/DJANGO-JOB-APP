from django.shortcuts import render
from django.http import JsonResponse
from qualifications.models import Qualifications
# Create your views here.
def qualifcations(request):
    return render(request,'qualifcations.html')
def submitQualification(request):
    if request.session.get('first_name', None) is not None:
        name=request.POST["name"]
        Description=request.POST["Description"]
        color=request.POST["color"]
        if  Qualifications.objects.filter(name=name):
            return JsonResponse({
                "type":"Warning",
                "message":"Please the name is already exist !!"
            })
        if  Qualifications.objects.filter(Description=Description):
            return JsonResponse({
                "type":"Warning",
                "message":"Please the Description is already exist !!"
            })
        q=qualifications(name=name,Description=Description,color=color)
        q.save()
        return JsonResponse({
            "type":"Success",
            "message":"Addedd with success !!"
        })
    else:
        return JsonResponse({
            "type":"Warning",
            "message":"Unauthorized Request !!"
        })