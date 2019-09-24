from django.urls import path,re_path,include
from Seller.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('register/', cache_page(60*5)(register)),
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
    path('get_task/', get_task),
    path('mtv/', middle_test_view),

    # 订单
    re_path(r"order_list/(?P<status>\d{1})",order_list),
    path("change_order/",change_order),# 改变订单状态

    #销售统计
    path("sales_sta/",sales_sta)


    # path('goods_update/', goods_update),
]

