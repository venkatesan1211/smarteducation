from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Homepage(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')

def studentlogin(request):
    return render(request,'studentlogin.html')


def stafflogin(request):
    return render(request,'stafflogin.html')


def studentdashboard(request):
    return render(request,'studentdashboard.html')

def staffdashboard(request):
    return render(request,'staffdashboard.html')


def layout(request):
    return render(request,'layouts.html')

def account(request):
    return render(request,'account.html')

def studentregister(request):
    return render(request,'studentregister.html')


def staffregister(request):
    return render(request,'staffregister.html')

def forgotpassword(request):
     return render(request,'forgotpassword.html')