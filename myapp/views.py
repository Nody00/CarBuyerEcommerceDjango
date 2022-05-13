from random import Random, random
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Cars, Person
import mysql.connector as sql


# Create your views here.

def loginuser(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='autodilerdata')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from Person where username='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'test.html')
        else:
            return render(request,"home.html")

    return render(request,'login.html')

#def loginuser(request):   Didnt work,sql connector was not used
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Person.empAuth_objects.get(request, username=Person.username, password=Person.password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,"There was an error try again")
            return redirect('login')
    else:
        return render(request,'login.html')








    
    


def test(request):
    persons=Person.objects.all()
    context={
        'persons':persons
    }
    return render(request,'test.html',context)






def register(request):
    if request.method=='POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('city') and request.POST.get('username') and request.POST.get('password'):
            saverecord=Person()
            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.city=request.POST.get('city')
            saverecord.username=request.POST.get('username')
            saverecord.password=request.POST.get('password')
            saverecord.carid=0
            saverecord.personid=0
            saverecord.save()
            messages.success(request,"Profile created successfuly!")
            return render(request,'register.html')
    else:
            return render(request,'register.html')
      

def home(request):
    cars=Cars.objects.all()
    context={
        'cars':cars
    }
    return render(request,'home.html',context)
    
def sell(request):
    if request.method=='POST':
        if request.POST.get('model') and request.POST.get('manufacturer') and request.POST.get('model_year') and request.POST.get('fuel_type') and request.POST.get('engine_size') and request.POST.get('body_type') and request.POST.get('trans'):
            saverecord=Cars()
            saverecord.model=request.POST.get('model')
            saverecord.manufacturer=request.POST.get('manufacturer')
            saverecord.model_year=request.POST.get('model_year')
            saverecord.fuel_type=request.POST.get('fuel_type')
            saverecord.engine_size=request.POST.get('engine_size')
            saverecord.body_type=request.POST.get('body_type')
            saverecord.transmission=request.POST.get('trans')
            saverecord.carid=0
            saverecord.save()
            messages.success(request,"You're car is now on sale")
            return render(request,'sell.html')
    else:
            return render(request,'sell.html')

    


    
    
    