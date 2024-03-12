"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('index',views.index),
    path('file',views.file),
    
    path('signup',views.signup),
    path('login',views.login),
    
    path('patient',views.patient),
    path('login_validate',views.login_validate),
    path('patiant_dashbord',views.patiant_dashbord),
    path('plogout',views.plogout),
    
    path('docter',views.docter),
    path('Docter_validate',views.Docter_validate),
    path('Docter_dashbord',views.Docter_dashbord),
    
    path('deletepatiant',views.deletepatiant),
    path('profileupdate',views.profileupdate),
    path('profilesubmit',views.profilesubmit),
    path('logout',views.logout),
    
    path('alllogin',views.alllogin),
    
    
    
    # path('savefile',views.savefile),
    
    
    path('',views.home),
    path('about/',views.about),
    path('departments/',views.departments),
    path('doctors/',views.doctors),
    path('contact/',views.contact),
    
    
    

   
]
