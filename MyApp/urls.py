
from unicodedata import name
from django import views
from django.urls import path,include
from .import views
from MyApp.views import *
urlpatterns = [
    
    
    path('',RegisterCreate.as_view(),name='register'),
    path('details/',views.all_details,name='alldetails'),
]