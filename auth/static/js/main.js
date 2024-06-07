var token=document.getElementsByName('csrfmiddlewaretoken')[0].value
function loginUser(){
    var email=document.getElementById("email").value;
    var password=document.getElementById("password").value;
    if(email!="" && password!=""){
        var f=new FormData();
        f.append("email",email);
        f.append("password",password);
        f.append("csrfmiddlewaretoken",token)
        var xhr=new XMLHttpRequest();
        xhr.onreadystatechange=function(){
            if(this.status==200 && this.readyState==4){
                var {message,type}=JSON.parse(this.responseText);
                if(type=="Success"){
                    
                    toastr.success(message,type,{positionClass:"toast-bottom-right"});
                    document.getElementById("email").value="";
                    document.getElementById("password").value="";
                    window.location.href="/"
                }
                if(type=="Warning")
                     toastr.warning(message,type,{positionClass:"toast-bottom-right"});

            }
        }
        xhr.open("POST","loginUser",true);
        xhr.send(f);

    }else{
        toastr.warning("All the fields are required !!","Warning",{positionClass:"toast-bottom-right"});

    }
}
function signIng(){
    var first_name=document.getElementById("first_name").value;
    var last_name=document.getElementById("last_name").value;
    var phone=document.getElementById("phone").value;
    var email=document.getElementById("email").value;
    var password=document.getElementById("password").value;
    if(first_name!="" && last_name!="" &&
    phone!="" &&
    email!="" &&
    password!=""){
            var f=new FormData();
            f.append("email",email);
            f.append("password",password);
            f.append("csrfmiddlewaretoken",token)
            f.append("first_name",first_name);
            f.append("last_name",last_name);
            f.append("phone",phone);
            var xhr=new XMLHttpRequest();
            xhr.onreadystatechange=function(){
                if(this.status==200 && this.readyState==4){
                    var {message,type}=JSON.parse(this.responseText);
                    if(type=="Success"){
                        
                        toastr.success(message,type,{positionClass:"toast-bottom-right"});
                        document.getElementById("first_name").value="";
                        document.getElementById("last_name").value="";
                        document.getElementById("phone").value="";
                        document.getElementById("email").value="";
                        document.getElementById("password").value="";
    
                    }
                    if(type=="Warning")
                         toastr.warning(message,type,{positionClass:"toast-bottom-right"});
    
                }
            }
            xhr.open("POST","signinUser",true);
            xhr.send(f);
        // toastr.success("message","Succès",{positionClass:"toast-bottom-right"});
    }else{
        toastr.warning("All the fields are required !!","Warning",{positionClass:"toast-bottom-right"});
        
    }
   
}
function submitQualification(){
    var name=document.getElementById("name").value;
    var Description=document.getElementById("Description").value;
    var color=document.getElementById("color").value;
    if(name!="" && Description!="" && color!=""){
        var f=new FormData()
        f.append("name",name)
        f.append("Description",Description);
        f.append("color",color);
        f.append("csrfmiddlewaretoken",token)

        var xhr=new XMLHttpRequest();
        xhr.onreadystatechange=function(){
            if(this.status==200 && this.readyState==4){
                var {message,type}=JSON.parse(this.responseText);
                if(type=="Success"){
                    
                    toastr.success(message,type,{positionClass:"toast-bottom-right"});
                    document.getElementById("name").value="";
                    document.getElementById("Description").value="";
                    document.getElementById("color").value="";
                }
                if(type=="Warning")
                     toastr.warning(message,type,{positionClass:"toast-bottom-right"});

            }

            }
            xhr.open("POST","submitQualification",true);
            xhr.send(f);
            
        
    }else{
        toastr.warning("All the fields are required !!","Warning",{positionClass:"toast-bottom-right"});
    }
}