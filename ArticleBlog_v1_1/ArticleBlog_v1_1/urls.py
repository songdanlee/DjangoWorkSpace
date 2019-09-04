"""ArticleBlog_v1_1 URL Configuration

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
from django.urls import path,re_path,include
from django.views.static import serve
from ArticleBlog_v1_1.views import *
# from Article.views import *
from ArticleBlog_v1_1.settings import MEDIA_ROOT


urlpatterns = [

    path('admin/', admin.site.urls),
    re_path('^media/(?P<path>.*)$', serve,{"document_root":MEDIA_ROOT}),
    path('index/', index),
    re_path(r"^$", index),

    re_path(r'newList/(?P<types>\w+)/(?P<p>\d{1,3})', newList),
    re_path('about', about),
    re_path('content/(?P<id>\d{1,3})', content),


    path('listpic/', img),
    # path('img/', img, name='img'),
    path('getImgs/', getImgs, name='getImgs'),


    # path("request_method/",request_method),

    # path("form_get/",form_get),
    path("form_post/",form_post),

    path("register/",register),

    # path("jq_exam/",jq_exam),
    # path("ajaxgetdata/",ajax_get_page),

    # path("jq_post_exam/",jq_post_exam),
    # path("ajaxpostdata/",ajax_post_page),
    path("register_check/",register_check), # ajax检测邮箱是否存在
    path("login/",login),
    path("login_check/",login_check),
]
