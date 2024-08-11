from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as user_auth, logout
from django.contrib import auth



# Create your views here.

def llb(request):
    return render(request,'llb.html')


def signup(request):
    
    if request.method == "POST":

        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # print(uname,email,fname,lname,pass1,cpass)

        try:
            if User.objects.get(username=email):
                messages.error(request,"Username is taken..")
                return redirect('signup')
        except:
            pass

        myuser = User.objects.create_user(email, uname, password)
        myuser.save()
        messages.success(request,"Signup Success")
        return redirect('login')

    return render(request, "register.html")



def login(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # print(email,pass1)
        myuser = authenticate(username=email, password=password)

        if myuser is not None:
            user_auth(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('home')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')

    return render(request, "logn.html")  



def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('First_name','default')
        lastname = request.POST.get('Last_name','default')
        email = request.POST.get('Email','default')
        number = request.POST.get('Number','default')
        date = request.POST.get('Date','default')
        image = request.FILES.get('Student_Image')
        
        information = Student_information(First_name=firstname, Last_name=lastname, Email=email, Number=number, Date=date,Student_Image=image)
        information.save()
        
        messages.success(request,f"{firstname} Register successfully...!")   
        return redirect('showino')
    return render(request,'home.html')



def showino(request):
    student = Student_information.objects.all()    
    param={'students':student}
    return render(request,'showino.html',param)



def delete(request,id):
    delete = Student_information.objects.get(student_id=id)
    delete.delete()
    messages.success(request,"Data Deleted successfully...!")  
    return redirect('showino')



def update(request,id):
    update = Student_information.objects.get(student_id=id)
    
    if request.method == 'POST':
        update.firstname = request.POST.get('First_name','default')
        update.lastname = request.POST.get('Last_name','default')
        update.email = request.POST.get('Email','default')
        update.number = request.POST.get('Number','default')
        update.date = request.POST.get('Date','default')
        if request.FILES.get('Student_Image'):
            update.Student_Image = request.FILES.get('Student_Image')
        
        update.save()
        messages.success(request, "Data updated successfully...!")
        return redirect('showino') 
    
    param={'First_name':update.First_name,'Last_name':update.Last_name,'Email':update.Email,'Number':update.Number,'Date':update.Date,'Student_Image':update.Student_Image}    
    return render(request,'update.html',param) 
