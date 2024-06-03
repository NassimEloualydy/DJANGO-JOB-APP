from django.shortcuts import render
from users.models import User
from django.http import JsonResponse
import hashlib
def logout(request):
       del request.session['first_name']
       del request.session['last_name']
       del request.session['email']
       del request.session['password']
       del request.session['phone']

       return render(request,'index.html')

def loginUser(request):
    email=request.POST['email']
    password=request.POST['password']
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    if not User.objects.filter(email=email,password=md5_hash.hexdigest()):
        return JsonResponse({
            "type":"Warning",
            "message":"The email or the password is wrong !!"
        })
    u=User.objects.filter(email=email,password=md5_hash.hexdigest()).first()
    u.status="Connected"
    u.save()
    request.session['first_name']=u.first_name
    request.session['last_name']=u.last_name
    request.session['email']=u.email
    request.session['password']=u.password
    request.session['phone']=u.phone
    request.session['status']=u.status
    request.session['role']=u.role
    
    return JsonResponse({
            "type":"Success",
            "message":"Connected with Success"
        })

    
    
    
def signinUser(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    password=request.POST["password"]
    if User.objects.filter(first_name=first_name,last_name=last_name).exists():
                    return JsonResponse({
                        "type": "Warning",
                        "message": "The first name and the last name is already exist !!"
                    })
    if User.objects.filter(phone=phone).exists():
                    return JsonResponse({
                        "type": "Warning",
                        "message": "The phone is already exist !!"
                    })
    if User.objects.filter(email=email).exists():
                    return JsonResponse({
                        "type": "Warning",
                        "message": "The email is already exist !!"
                    })
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    u=User(status="Disconnected",role="user",first_name=first_name,last_name=last_name,phone=phone,email=email,password=md5_hash.hexdigest())
    u.save()
    return JsonResponse({
                        "type": "Success",
                        "message": "Created with success !!"
                    })

