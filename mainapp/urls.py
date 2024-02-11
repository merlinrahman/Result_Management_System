from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

    # ***************************************
                 # HOME PAGE
    #*****************************************
    path('', views.index, name='index'),

    # ***************************************
                 # ABOUT PAGE
    #*****************************************
    path('about/', views.about, name='about'),

               # CONTACT PAGE
    #*****************************************
    path('contact/', views.contact, name='contact'),

]