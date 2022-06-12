from django.shortcuts import redirect
from django.urls import path
from django.views import View
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
   # path('', views.index),

    
    path("",views.index),
    path("result",views.show),
    





]

