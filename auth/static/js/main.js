var token=document.getElementsByName('csrfmiddlewaretoken')[0].value
var id_qualification=0
var offset_qualification=0
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
        f.append("DescriptionQ",Description);
        f.append("color",color);
        f.append("csrfmiddlewaretoken",token)
        f.append("id",id_qualification);
        var xhr=new XMLHttpRequest();
        xhr.onreadystatechange=function(){
            if(this.status==200 && this.readyState==4){
                var {message,type}=JSON.parse(this.responseText);
                if(type=="Success"){
                    
                    toastr.success(message,type,{positionClass:"toast-bottom-right"});
                    document.getElementById("name").value="";
                    document.getElementById("Description").value="";
                    document.getElementById("color").value="";
                    getDataQulaifications()
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
function getDataQulaifications(){
if(document.getElementById("dataQualification")){

    var name=document.getElementById("name_search").value;
    var Description=document.getElementById("description_search").value;
    var color=document.getElementById("color_search").value;
    var f=new FormData()
    f.append("name",name)
    f.append("Description",Description)
    f.append("color",color)
    f.append("offset",offset_qualification);
    f.append("csrfmiddlewaretoken",token)
    var xhr=new XMLHttpRequest()
    xhr.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            var {message,data}=JSON.parse(this.responseText);
            var dataFrontEnd=""
            if(data.length>0){
                for(var i=0;i<data.length;i++){
                    dataFrontEnd+="<tr><td>"+data[i][0]+"</td>"
                    dataFrontEnd+="<td>"+data[i][1]+"</td>"
                    dataFrontEnd+="<td>"+data[i][2]+"</td>"
                    dataFrontEnd+="<td>"+data[i][3]+"</td>"
                    dataFrontEnd+="<td><ion-icon  class='Icon Icon_delete' onclick='deleteQualification("+data[i][0]+")' name='trash-outline'></ion-icon></td><td><ion-icon   class='Icon Icon_update' onclick='loadDataQualification("+JSON.stringify(data[i])+");' data-bs-toggle='modal' data-bs-target='#modalDomain' name='pencil-outline'></ion-icon></td>"
                    dataFrontEnd+="</tr>"
                }
                document.getElementById("dataQualification").innerHTML=dataFrontEnd
            }else{
                offset_qualification-=6
                getDataQulaifications()
            }
        }
    }
    xhr.open("POST","getDataQualifications",true);
    xhr.send(f);
}

}
function deleteQualification(id){
    var f=new FormData()
    f.append("id",id)
    f.append("csrfmiddlewaretoken",token)
    var xhr=new XMLHttpRequest()
    xhr.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            var {message,type}=JSON.parse(this.responseText);
            if(type=="Success"){
                        
                toastr.success(message,type,{positionClass:"toast-bottom-right"});
                getDataQulaifications()
            }
            if(type=="Warning")
                 toastr.warning(message,type,{positionClass:"toast-bottom-right"});


        }
    }
    xhr.open("POST","deleteQualifications",true);
    xhr.send(f);
        
}
function loadDataQualification(data){
    
    document.getElementById("name").value=data[1];
    document.getElementById("Description").value=data[2];
    document.getElementById("color").value=data[3];
    id_qualification=data[0]
    document.getElementById("submitDeviceButton").innerHTML="Update";

}
function hideDataQualifiation(){
    document.getElementById("name").value="";
    document.getElementById("Description").value="";
    document.getElementById("color").value="";
    id_qualification=0
    document.getElementById("submitDeviceButton").innerHTML="Add";
}
function navigateDataContacts(data){
    if(data=="next"){
        offset_qualification+=6
    }
    if(data=="prev" && offset_qualification>0){
        offset_qualification-=6

    }
    getDataQulaifications();
}   
function submitCategory(){
    var name=document.getElementById("name").value;
    var description=document.getElementById("description").value;
    if(name!="" && description!=""){
        var xhr=new XMLHttpRequest();
        xhr.onreadystatechange=function(){
            if(this.status==200 && this.readyState==4){
                var {message,type}=JSON.parse(this.responseText);
                if(type=="Success"){
                            
                    toastr.success(message,type,{positionClass:"toast-bottom-right"});
                    getDataQulaifications()
                }
                if(type=="Warning")
                     toastr.warning(message,type,{positionClass:"toast-bottom-right"});
    
               }
        }
        xhr.open("POST","addCategory",true);
        var f=new FormData();
        f.append("name",name);
        f.append("description",description);
        f.append("csrfmiddlewaretoken",token)
        xhr.send(f)
    }else{
        toastr.warning("Please all the field required !!","Warning",{positionClass:"toast-bottom-right"})
    }
}