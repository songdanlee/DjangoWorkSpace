from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [

    path('register/', register),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('user_info/', user_info),
    #path('good_list/', good_list),
    re_path('good_list/(?P<page>\d+)/', good_list),
    re_path('good_detail/(?P<id>\d+)/', good_detail)
]

