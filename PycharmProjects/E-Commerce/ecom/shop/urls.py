# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="aboutUs"),
    path('contact/', views.contact, name="contactus"),
    path('tracker/', views.tracker, name="trackingstatus"),
    path('search/', views.search, name="search"),
    path('productView/', views.productView, name="view"),
    path('checkout/', views.checkout, name="checkout")
]
