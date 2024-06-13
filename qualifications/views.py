from django.shortcuts import render
from django.http import JsonResponse
from qualifications.models import Qualifications
from django.db import connection

# Create your views here.
def deleteQualifications(request):
    if request.session.get("first_name",None) is None :
        return JsonResponse({
            "type":"Danger",
            "message":""
        })
    id=request.POST["id"]
    q=Qualifications.objects.filter(id=id).first()
    q.delete()
    return JsonResponse({
            "type":"Success",
            "message":"Deleted with success !!"
        })

def getDataQualifications(request):
    if request.session.get('first_name', None) is None:
        return JsonResponse({
            "type":"Danger",
            "data":"Loged in please"
        })
    name=request.POST["name"]
    Description=request.POST["Description"]
    color=request.POST["color"]
    offset=request.POST["offset"]
    
    cursor = connection.cursor()
    query="SELECT q.id,q.name,q.description,q.color from public."+'"'+"qualifications_qualifications"+'"'+" as q"
    query+=" INNER JOIN public."+'"'+"qualifications_qualifications"+'"'+" as q1 on q1.id=q.id"
    query+=" INNER JOIN public."+'"'+"qualifications_qualifications"+'"'+" as q2 on q2.id=q.id"
    query+=" INNER JOIN public."+'"'+"qualifications_qualifications"+'"'+" as q3 on q3.id=q.id"
    query+=" where q1.name like '%"+name+"%' and "
    query+="  q2.description like '%"+Description+"%' and "
    query+="  q3.color like '%"+color+"%' OFFSET "+offset+" limit 6 "
    cursor.execute(query)
    return JsonResponse({
            "type":"Success",
            "data":cursor.fetchall()
        })
def qualifcations(request):
    return render(request,'qualifcations.html')
def submitQualification(request):
    if request.session.get('first_name', None) is not None:
        name=request.POST["name"]
        Description=request.POST.get("DescriptionQ",False)
        color=request.POST["color"]
        id_q=request.POST["id"]
        if id==0:
            if  Qualifications.objects.filter(name=name):
                return JsonResponse({
                    "type":"Warning",
                    "message":"Please the name is already exist !!"
                })
            if  Qualifications.objects.filter(description=Description):
                return JsonResponse({
                    "type":"Warning",
                    "message":"Please the Description is already exist !!"
                })
            q=Qualifications(name=name,description=Description,color=color)
            q.save()
        else:
           if  Qualifications.objects.filter(name=name).exclude(pk=id_q):
                print("hHHAHAHAHA")
                return JsonResponse({
                    "type":"Warning",
                    "message":"Please the name is already exist !!"
                })
           if  Qualifications.objects.filter(description=Description).exclude(pk=id_q):
                return JsonResponse({
                    "type":"Warning",
                    "message":"Please the Description is already exist !!"
                })
           q=Qualifications.objects.filter(pk=id_q).first()
           q.name=name
           q.description=Description
           q.color=color
           q.save()

        return JsonResponse({
            "type":"Success",
            "message":"Updated with success !!"
        })
    else:
        return JsonResponse({
            "type":"Warning",
            "message":"Unauthorized Request !!"
        })