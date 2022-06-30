from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("This is the about section of the shop")
def search(request):
    return Search("Pls enter something to search for ")

def contact(request):
    return HttpResponse("You can contact me at 8209809740")

def tracker(request):
    return HttpResponse("Your order is in transit")

def productView(request):
    return HttpResponse("This is ryzen 9 6900HX laptop with 32 gb of ram ")

def checkout(request):
    return HttpResponse("Your bill is $1200")
