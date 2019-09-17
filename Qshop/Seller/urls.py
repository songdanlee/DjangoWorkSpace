from django.urls import path,re_path,include
from Seller.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('register/', register),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('goods_list/', goods_list),
    path('personal_info/', personal_info),
    re_path('goods_list/(?P<page>\d+)/(?P<status>\w+)/', goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)/', goods_status),
    path('goods_add/', goods_add),
    path('slc/', send_login_code),
    path('send_eamil_code/', send_eamil_code),
    # path('goods_update/', goods_update),
]

