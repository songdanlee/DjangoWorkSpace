"""DjangoLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from LoginUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('goods_list/', goods_list),
    re_path('goods_list/(?P<page>\d+)/(?P<status>\w+)/', goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)/', goods_status),
    # path('goods_add/', goods_add),
    # path('goods_update/', goods_update),
]


from django.views.decorators.csrf import csrf_exempt


urlpatterns += [
    re_path('goods_list_api/(?P<page>\d+)/(?P<status>\w+)/', goods_list_api),
    path('vue/', vue),
    path('goods/', csrf_exempt(Goods.as_view())),
]

