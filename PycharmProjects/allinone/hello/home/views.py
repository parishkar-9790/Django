from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':'this is sent '
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse("this is about section of the website")
def services(request):
    return HttpResponse("This is services page")