from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,'./login.html')

def signup(request):
    return render(request,'./signup.html')

def success(request):
    name=request.POST['name']
    phone=request.POST['phone']
    mail=request.POST['mail']
    uname=request.POST['uname']
    password=request.POST['password']
    confirm=request.POST['confirm']

    #phone valoidation
    phoneFlag=False
    if len(phone)==10 and phone[0] in '6789':
        phoneFlag=True
    
    #mail valuidation 
    mailFlag=False
    upper=0
    special=0
    for char in mail:
        if char.isupper():
            upper+=1
        if char=='@':
            special+=1
    if upper==0 and special==1:
        mailFlag=True

    #username validation
    userFlag=False
    try:
        Details.objects.filter(USERNAME=uname)
    except:
        userFlag=True

    #password validation
    passwordFlag=False
    u=0
    l=0
    n=0
    s=0
    
    for char in password:
        if char.isupper():
            u+=1
        elif char.islower():
            l+=1
        elif char.isdigit():
            n+=1
        else:
            s+=1
    if 8<=len(password)<=16 and u>=1 and l>=1 and n>=1 and s>=1:
        passwordFlag=True

    #confirm password
    confirmFlag=False
    if confirm==password:
        confirmFlag=True

    if phoneFlag==True and mailFlag==True and userFlag==True and  passwordFlag==True and confirmFlag==True:
        obj=Details()
        obj.NAME=name
        obj.PHONE=phone
        obj.EMAIL=mail
        obj.USERNAME=uname
        obj.PASSWORD=password
        obj.save() 
        return render(request,'./success.html')
    else:
        return render(request,'./signup.html', context={'result':'invalid error'})

def forgot(request):
    return render(request,'./forgot.html')

def updateforgot(request):
    phone=request.POST['phone']
    password=request.POST['password']
    confirm=request.POST['confirm']

    try:
        data=Details.objects.get(PHONE=phone)
        if password==confirm:
            data.PASSWORD=password
            data.save()
            return render(request,'./success.html')
        else:
            return render(request,'./forgot.html', context={'error':"password doen't matchh.. re-enter"})
    except:
        return render(request,'./forgot.html', context={'error':"You are not a exiting user"})


def homepage(request):
    name=request.POST['name']
    password=request.POST['password']
    try:
        Details.objects.get(USERNAME=name, PASSWORD=password)
        return render(request,'./home.html',context={'error':"Logged successfully"})
    except:
        return render(request,'./login.html', context={'error':"Username and Password incorect"})
        

def cookie(request):
    response=HttpResponse('cookies set....!!')
    response.set_cookie('apple','iphone 15 pro max uhh!')
    return response