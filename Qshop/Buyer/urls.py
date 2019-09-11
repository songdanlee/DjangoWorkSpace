from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [

    path('register/', register),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('user_info/', user_info),
    path('user_order/', user_order),
    path('user_site/', user_site),
    path('alipayOrder/', alipayOrder),
    path('pay_result/', pay_result),
    #path('good_list/', good_list),
    re_path('good_list/(?P<page>\d+)/', good_list),
    re_path('good_detail/(?P<id>\d+)/', good_detail),
    re_path('pay_order/', pay_order),
]

