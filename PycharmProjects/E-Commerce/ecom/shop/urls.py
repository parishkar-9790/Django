# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('contact/', views.contact, name="contactus"),
    path('about/', views.about, name="aboutus"),
    path('tracker/', views.tracker, name="trackingstatus"),
    path('search/', views.search, name="search"),
    path('productview/', views.prodView, name="view"),
    path('checkout/', views.checkout, name="checkout")
]
