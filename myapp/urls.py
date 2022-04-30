from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginuser,name='login'),
    path('test', views.test,name='test'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home')
    
]