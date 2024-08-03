from django.shortcuts import render
from django.http import JsonResponse
from qualifications.models import Qualifications
from django.db import connection
from categoryJob.models import Category
# Create your views here.
def category(request):
    return render(request,"category.html")
def addCategory(request):
    if request.session.get('first_name',None) is not None:
        name=request.POST["name"]
        description=request.POST["description"]
        id_pk=request.POST["id"]
        if id_pk==0:
            if  Category.objects.filter(name=name):
                return JsonResponse({
                    "type":"Warning",
                    "message":"The name is already exist !!"
                })           
            if Category.objects.filter(description=description):
                return JsonResponse({
                    "type":"Warning",
                    "message":"The description is already exist !!"
                }) 
            c=Category(name=name,description=description)
            c.save()
            return JsonResponse({
                "type":"Success",
                "message":"Category added with success "
            })
        else:
            if  Category.objects.filter(name=name).exclude(pk=id_pk):
                return JsonResponse({
                    "type":"Warning",
                    "message":"The name is already exist !!"
                })           
            if Category.objects.filter(description=description).exclude(pk=id_pk):
                return JsonResponse({
                    "type":"Warning",
                    "message":"The description is already exist !!"
                }) 
            c=Category.objects.filter(id=id_pk).first()
            c.name=name
            c.description=description

            c.save()
            return JsonResponse({
                "type":"Success",
                "message":"Category updated with success "
            })

    else:
        return JsonResponse({
            "type":"Warning",
            "message":"Unuathorized Request !!"
        })
    return

def getdataCategories(request):
    if request.session.get('first_name',None) is None:
        return JsonResponse({
            "type":"Danger",
            "message":"Loged In please"
        })
    name=request.POST['name']
    offset=request.POST['offset']
    description=request.POST['Description']

    cursor=connection.cursor()
    query="SELECT c.id,c.name,c.Description from public."+'"'+"categoryJob_category"+'"'+" as c"
    query+=" INNER JOIN public."+'"'+"categoryJob_category"+'"'+" as c1 on c1.id=c.id"
    query+=" INNER JOIN public."+'"'+"categoryJob_category"+'"'+" as c2 on c2.id=c.id"
    query+=" WHERE c1.name like '%"+name+"%' and c2.Description like '%"+description+"%' offset "+offset+" limit 6 "
    cursor.execute(query)
    DATA=cursor.fetchall()
    return JsonResponse({
        "message":"full" if len(DATA)>0 else "empty",
        "type":"Success",
        "data":DATA
    })
def deleteCategory(request):
    if request.session.get('first_name',None) is None:
        return JsonResponse({
            "type":"Danger",
            "message":"Please loged in"
        })
    id=request.POST['id']
    c=Category.objects.filter(id=id).first()
    c.delete()
    return JsonResponse({
        "type":"Success",
        "message":"Deleted with success !!"
    })