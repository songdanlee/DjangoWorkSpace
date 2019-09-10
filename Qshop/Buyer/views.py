from django.shortcuts import render
from django.http import HttpResponseRedirect
from Seller.models import *
from Seller.views import getPassword
# Create your views here.

def loginValid(func):
    """
    :desc 闭包函数校验是否登录
    :param func:
    :return:
    """

    def inner(request, *args, **kwargs):
        email = request.COOKIES.get("user")


        if email and id:
            user = LoginUser.objects.filter(email=email).first()
            if user:
                return func(request, *args, **kwargs)
        return HttpResponseRedirect("/Seller/login/")

    return inner

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        user = LoginUser.objects.filter(email=email).first()
        if user:
            db_password = user.password
            pwd = getPassword(pwd)
            if db_password == pwd:
                response = HttpResponseRedirect("/Buyer/index/",locals())
                response.set_cookie("user", user.email)
                response.set_cookie("username", user.username)
                return response
    return render(request,"buyer/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")

        user = LoginUser()
        user.username = username
        user.password = getPassword(pwd)
        user.email = email
        user.save()
        return HttpResponseRedirect("/Buyer/login/",locals())
    return render(request,"buyer/register.html")

def index(request):
    types = GoodsType.objects.all()
    goods_result = []
    for type in types:
        goods = type.goods_set.all()[0:4]
        if len(goods) >= 4:
            goods_result.append({type:goods})
    return render(request,"buyer/index.html",locals())



def logout(request):

    response = HttpResponseRedirect("/Buyer/index/")
    cookies = request.COOKIES.keys()
    for cookie in cookies:
        response.delete_cookie(cookie)

    return response
