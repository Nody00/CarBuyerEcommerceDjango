from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.

def login(request):

    
    return render(request,'login.html')


def test(request):
    persons=Person.objects.all()
    context={
        'persons':persons
    }
    return render(request,'test.html',context)