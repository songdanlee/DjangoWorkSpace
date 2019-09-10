from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [

    path('register/', register),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
]

