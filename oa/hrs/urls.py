from django.urls import path

from hrs.views import *

urlpatterns = [
        path("",index,name="index")
        ]       
