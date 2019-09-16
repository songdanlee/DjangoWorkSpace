from django.urls import path,re_path
from Buyer.views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    path('register/', register),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('user_info/', user_info),
    path('user_order/', user_order),
    path('user_site/', user_site),
    path('alipayOrder/', alipayOrder), # 支付宝支付页
    path('pay_result/', pay_result), # 支付成功返回页
    re_path('good_list/(?P<page>\d+)/', good_list),
    re_path('good_detail/(?P<id>\d+)/', good_detail),
    re_path('pay_order/', csrf_exempt(pay_order)), # 订单页
    re_path('add_cart/',add_cart), # 购物车


    path('mycart/',mycart)
]

