from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.Homepage,name='Homepage'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('courses', views.courses,name='courses'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('stafflogin',views.stafflogin,name='stafflogin'),
    path('studentdashboard',views.studentdashboard,name='studentdashboard'),
    path('staffdashboard',views.staffdashboard,name='staffdashboard'),
    path('layout',views.layout,name='layout'),
    path('account',views.account,name='account'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('staffregister',views.staffregister,name='staffregister'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
]