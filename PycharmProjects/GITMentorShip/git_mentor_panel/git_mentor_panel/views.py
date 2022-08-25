from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('dean_home')
            elif user_type == '2':
                return HttpResponse("This is mentor panel")
            elif user_type == '3':
                return HttpResponse("This is student panel")
            else:
                # return Http('This is wrong password')
                messages.error(request, "Email and Password are invalid! ")
                return redirect('login')
        else:
            messages.error(request, "Email and Password are invalid!")
            return redirect('login')


def doLogout(request):
   logout(request)
   return redirect('login')
@login_required(login_url='/')
def PROFILE(request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
        'user':user
    }
    # print(user)
    return render(request,'profile.html',context)
def PROFILE_UPDATE(request):
    if request.method=="POST":
        profile_pic=request.FILE.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        print(profile_pic,first_name,last_name,email)
    return render(request,'profile.html')