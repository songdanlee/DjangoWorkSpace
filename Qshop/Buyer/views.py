from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
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
        s_email = request.session.get("user")
        if email and s_email and email == s_email:
            user = LoginUser.objects.filter(email=email).first()
            if user:
                return func(request, *args, **kwargs)
        return HttpResponseRedirect("/Buyer/login/")

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

                response = HttpResponseRedirect("/Buyer/index/", locals())
                response.set_cookie("user", user.email)
                response.set_cookie("username", user.username)
                request.session["user"] = user.email
                return response
    return render(request, "buyer/login.html")


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
        return HttpResponseRedirect("/Buyer/login/", locals())
    return render(request, "buyer/register.html")


def index(request):
    types = GoodsType.objects.all()
    goods_result = []
    for type in types:
        goods = type.goods_set.order_by("goods_pro_date")[0:4]
        if len(goods) >= 4:
            goods_result.append({type: goods})
    return render(request, "buyer/index.html", locals())


def logout(request):
    url = request.META.get("HTTP_REFERER","/Buyer/index/")
    response = HttpResponseRedirect(url)
    cookies = request.COOKIES.keys()
    for cookie in cookies:
        response.delete_cookie(cookie)
    if request.session.get("user"):
        del request.session['user']
    return response

@loginValid
def user_info(request):
    return render(request,"buyer/user_center_info.html",locals())

import math

"""
def good_list(request):
    type = request.GET.get("type")
    keyword = request.GET.get("keyword")
    goods_list = []
    if type == 'byid':
        if keyword:
            types = GoodsType.objects.get(id=keyword)
            goods_list = types.goods_set.order_by("goods_pro_date")
    elif type == 'bykey':
        if keyword:
            goods_list = Goods.objects.filter(goods_name__contains=keyword).order_by("goods_pro_date")
    if goods_list:
        nums = goods_list.count()
        nums = int(math.ceil(nums / 5))
        recommon_list = goods_list[:nums]
    return render(request, "buyer/goods_list.html", locals())

"""
def good_list(request,page):
    page = int(page)
    type = request.GET.get("type")
    keyword = request.GET.get("keyword")
    goods_list = []
    if type == 'byid': # 按照商品id查
        if keyword:
            types = GoodsType.objects.get(id=int(keyword))
            goods_list = types.goods_set.order_by("goods_pro_date")
    elif type == 'bykey': # 按商品名字查
        if keyword:
            goods_list = Goods.objects.filter(goods_name__contains=keyword).order_by("goods_pro_date")

    if goods_list:
        # 分页
        page_list = Paginator(goods_list, 15)
        goods_list = page_list.page(page)
        pages = page_list.page_range
        # 推荐商品
        nums = len(goods_list)
        nums = int(math.ceil(nums / 5))
        recommon_list = goods_list[:nums]

    return render(request, "buyer/goods_list.html", locals())


def good_detail(request,id):

    good = Goods.objects.filter(id = int(id)).first()
    return render(request,"buyer/detail.html",locals())