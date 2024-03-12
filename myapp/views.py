from django.shortcuts import render,HttpResponse,redirect
from .models import hospitaldash

# Create your views here.
def home(request):
    return render(request,"home.html")


def about(request):
    return render(request, "about.html")

def departments(request):
    return render(request, "departments.html")


def doctors(request):
    return render(request, "doctors.html")

def contact(request):
    return render(request, "contact.html")



def index(request):
		return render(request,"index.html")




# photo
def file(request):
    return redirect(request,'index.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        photo=request.FILES["photo"]
        # profile_picture=request.POST['profile_picture']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address_line1=request.POST['address_line1']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        
        
        
        s=hospitaldash(first_name=first_name,last_name=last_name,photo=photo,username=username,email=email,password=password,address_line1=address_line1,
                  city=city,state=state,pincode=pincode)
        s.save() ##insert quary
        
        
        # return HttpResponse("REGISTRATION SUCCESFULLY COMPLETED")
        return redirect("/login")
    else:
        # return HttpResponse("fail")
        return redirect("/")
    
    
    
# direct login page
def alllogin(request):
    return render(request,"login.html")

# petiant
   
def login(request):
    # if  request.method=="POST":
          return render(request,"login.html")
      
      
def patient(request):
    return render(request,"patient_login.html")



def login_validate(request):
    if request.method=='POST':   
        email=request.POST["email"]
        password=request.POST["password"]
        
        data=hospitaldash.objects.all().filter(email=email,password=password)
        
        
        if data:
        # if len(data)==1:   #duplicate element kadhayche astil tr te kadhane
            
            
            request.session["username"]=email   #session start
            
            return redirect("/patiant_dashbord")
        else:
             
              return redirect("/login")
          
          
          
def patiant_dashbord(request):
    if request.session.get("username") is not None:
        email=request.session.get('username')
        data=hospitaldash.objects.all().filter(email=email)
        return render(request,'patient_dash.html',{"data":data})
    else:
        return redirect("/patient")
        


def plogout(request):
    # del request.session["username"] #end session
    return redirect("/patient")


# docter url

def docter(request):
    return render(request,'Docter_login.html')


def Docter_validate(request):
     if request.method=='POST':   
        email=request.POST["email"]
        password=request.POST["password"]
        
        data=hospitaldash.objects.all().filter(email=email,password=password)
        
        
        if data:
        # if len(data)==1:   #duplicate element kadhayche astil tr te kadhane
            
            
            request.session["username"]=email   #session start
            
            return redirect("/Docter_dashbord")
        else:
             
              return redirect("/login")
          
          
          
def Docter_dashbord(request):
    data=hospitaldash.objects.all()  #select*from student 
    return render(request,'Docter_dash.html',{'data':data})
          



def deletepatiant(request):
    id=request.GET['id']
    
    hospitaldash.objects.all().filter(id=id).delete()  #delete queary
    return redirect("/Docter_dashbord")
    
   
def profileupdate(request):
    id=request.GET['id']
    data=hospitaldash.objects.filter(id=id)    #update query
    
    return render(request,"profile_update.html",{'data':data})


def profilesubmit(request):
    if request.method=='POST':
        id=request.POST['id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        photo=request.FILES["photo"]
        # profile_picture=request.POST['profile_picture']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address_line1=request.POST['address_line1']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        
        
        
        
        hospitaldash.objects.all().filter(id=id).update(first_name=first_name,last_name=last_name,photo=photo,username=username,email=email,password=password,address_line1=address_line1,
                  city=city,state=state,pincode=pincode)    ##update 
      
        return redirect("/Docter_dashbord")
    else:
        return redirect("/Docter_dashbord")
 

def logout(request):
    del request.session["username"]  #end session
    return redirect("/docter")


# image



        
        
        