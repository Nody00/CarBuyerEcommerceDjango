from random import Random
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Person

# Create your views here.

def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Person.empAuth_objects.get(request, username=Person.username, password=Person.password)
            if user is not None:
               login(request, user)
               return redirect('home')
            else:
                messages.success(request,"There was an error try again")
                return redirect('login')

        except Exception as identifier:
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
    return render(request,'home.html')



    
    
    