# coding=utf-8
import hashlib

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
from Seller.models import *


# Create your views here.

def getPassword(password):
    """
    :param password:  需要加密的密码
    :return:  MD5加密后的密文
    """
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


def register(request):
    """
    :param request:
    :description get请求返回注册页面，post请求，传入邮箱，密码，校验邮箱密码(邮箱未注册，邮箱和密码不为空)，返回注册成功信息
    :return: 注册成功返回注册成功信息，否则返回此页面，并提示错误信息
    """
    errormsg = ""
    successmsg = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        code = request.POST.get("valid_code")
        if email:  # 邮箱不为空
            user = LoginUser.objects.filter(email=email).first()  # 查找邮箱是否注册
            if not user:  # 未注册
                if password:  # 密码不为空
                    # 查询数据库用户当前最新的验证码
                    codes = Valid_Code.objects.filter(code_user=email).order_by("-code_time").first()
                    # 获取当前时间
                    now = time.mktime(datetime.datetime.now().timetuple())
                    # 获取验证码的存储时间
                    db_time = time.mktime(codes.code_time.timetuple())
                    # 时间差，换算为分钟
                    t = (now - db_time) / 60
                    """
                        验证码存在
                        验证码未过期
                        验证码未使用
                        输入验证码和数据库验证码一致（不区分大小写）    
                    """
                    if codes and t <= 5 and codes.code_state == 0 and code.upper() == codes.code_content.upper():
                        loginuser = LoginUser()
                        loginuser.username = email
                        loginuser.email = email
                        loginuser.password = getPassword(password)  # 加密数据
                        loginuser.save()  # 保存到数据库
                        successmsg = "恭喜你注册成功"
                    else:
                        errormsg = "验证码输入不正确"
                else:
                    errormsg = "密码为空"
            else:
                errormsg = "邮箱已被注册"
        else:
            errormsg = "邮箱为空"

    return render(request, "seller/register.html", locals())  # 未成功，返回错误信息


def loginValid(func):
    """
    :desc 闭包函数校验是否登录
    :param func:
    :return:
    """

    def inner(request, *args, **kwargs):
        username = request.COOKIES.get("username")
        id = request.COOKIES.get("id")
        session_username = request.session.get("session_username")
        if username and id:
            user = LoginUser.objects.filter(id=id).first()
            if user.username == username:
                return func(request, *args, **kwargs)
        return HttpResponseRedirect("/Seller/login/")

    return inner

import datetime
import time

def login(request):
    """
       :param request:
       :description get请求返回登录页面，post请求，传入邮箱，密码，校验邮箱密码(邮箱已注册，邮箱和密码不为空，密码与数据库匹配)，返回index页面
       :return: 登录成功返回index页面，否则重新登录
    """
    errormsg = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        code = request.POST.get("valid_code")
        if email:  # 邮箱不为空
            user = LoginUser.objects.filter(email=email).first()
            if user:  # 数据库可以查找到用户
                if password:  # 密码不为空
                    db_password = user.password  # 数据库中用户的密码
                    password = getPassword(password)  # 输入密码加密
                    if password == db_password:  # 密码正确,登录成功
                        # 查询数据库用户当前最新的验证码
                        codes = Valid_Code.objects.filter(code_user=email).order_by("-code_time").first()
                        # 获取当前时间
                        now = time.mktime(datetime.datetime.now().timetuple())
                        # 获取验证码的存储时间
                        db_time = time.mktime(codes.code_time.timetuple())
                        # 时间差，换算为分钟
                        t = (now - db_time) / 60
                        """
                            验证码存在
                            验证码未过期
                            验证码未使用
                            输入验证码和数据库验证码一致（不区分大小写）    
                        """
                        if codes and t <= 5 and codes.code_state==0 and code.upper() == codes.code_content.upper():
                            response = HttpResponseRedirect("/Seller/index/")
                            response.set_cookie("username", user.username)  # 添加cookie
                            response.set_cookie("id", user.id)
                            request.session['session_username'] = user.username  # 添加session
                            codes.code_state = 1 # 设置验证码已使用
                            codes.save()
                            return response  # 跳转到index首页
                        else:
                            if codes and t <= 5: # 过期
                                codes.code_state = 1 # 设置验证码已使用
                                codes.save()
                            errormsg = "验证码不正确"
                    else:
                        errormsg = "密码不正确"
                else:
                    errormsg = "密码为空"
            else:
                errormsg = "邮箱未注册"
        else:
            errormsg = "邮箱为空"

    return render(request, "seller/login.html", locals())


@loginValid
def index(request):
    """
    :desc 返回index页面
    :param request:
    :return:
    """

    return render(request, "seller/index.html", locals())


from django.core.paginator import Paginator


@loginValid
def goods_list(request, status="up", page=1):
    page = int(page)
    user_id = int(request.COOKIES.get("id"))
    user = LoginUser.objects.get(id=user_id)
    goods = Goods.objects.filter(goods_store=user)
    if status == "down":
        goods = goods.filter(goods_status=0)
    elif status == 'up':
        goods = goods.filter(goods_status=1)
    else:
        goods = goods.objects.all()
    goods_pagin = Paginator(goods, 10)
    goods_lists = goods_pagin.page(page)
    return render(request, "seller/goods_list.html", locals())


@loginValid
def goods_status(request, state, id):
    goods = Goods.objects.get(id=int(id))
    if state == 'up':  # 上架
        goods.goods_status = 1
    elif state == 'down':
        goods.goods_status = 0
    goods.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@loginValid
def personal_info(request):
    # 个人信息 展示
    id = int(request.COOKIES.get("id"))
    user = LoginUser.objects.get(id=id)

    if request.method == "POST":

        username = request.POST.get("username")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        phone_number = request.POST.get("phone_number")
        photo = request.FILES.get("photo")
        address = request.POST.get("address")

        if username:
            user.username = username
        if gender:
            user.gender = gender
        if age:
            user.age = age
        if phone_number:
            user.phone_num = phone_number
        if photo:
            user.photo = photo
        if address:
            user.address = address
        user.save()

    respon = render(request, "seller/personal_info.html", locals())
    respon.set_cookie("username", user.username)

    return respon


def logout(request):
    """
    :desc 退出登录
    :param request:
    :return:
    """
    response = HttpResponseRedirect("/Seller/login/")
    cookies = request.COOKIES
    print("清除cookie开始")
    for cookie in cookies.keys():
        print(cookie)
        response.delete_cookie(cookie)
    print("清除cookie结束")
    if request.session.get('session_username'):
        del request.session['session_username']
    return response


# 添加数据
@loginValid
def goods_add(request):
    if request.method == "POST":
        good = Goods()
        good.goods_num = request.POST.get("goods_num")
        good.goods_name = request.POST.get("goods_name")
        good.goods_price = request.POST.get("goods_price")
        good.goods_count = request.POST.get("goods_count")
        good.goods_location = request.POST.get("goods_location")
        good.goods_pro_date = request.POST.get("goods_pro_date")
        good.goods_save_month = request.POST.get("goods_save_month")
        good.goods_status = 1
        # 图片类型
        request.FILES
        picture = request.FILES.get("picture")
        good.goods_picture = picture
        # 外键，商品类型
        goods_id = int(request.POST.get("goods_type"))
        good.goods_type = GoodsType.objects.get(id=goods_id)
        # 商品店家
        user_id = int(request.COOKIES.get("id"))
        good.goods_store = LoginUser.objects.get(id=user_id)
        good.save()

    types = GoodsType.objects.all()
    return render(request, "seller/goods_add.html", locals())


from Seller.myutils import MailSender,random_code,sendDing as sd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CeleryTask.tasks import sendDing

@csrf_exempt
def send_login_code(request):
    result = {
        "code":200,
        "data":""
    }
    if request.method == "POST":
        email = request.POST.get("email")
        code = random_code()
        c = Valid_Code()
        c.code_user = email
        c.code_content = code
        c.save()
        send_data = "%s的验证码为%s,打死也不要告诉别人哟"%(email,code)
        #sd(send_data) # 发送验证
        # 使用celery异步任务
        sendDing.delay(send_data)
        result["data"] = "发送成功"
    else:
        result["code"] = 400
        result["data"] = "请求姿势不太对哟"
    return JsonResponse(result)

@csrf_exempt
def send_eamil_code(request):
    result = {
        "code": 200,
        "data": ""
    }
    if request.method == "POST":
        email = request.POST.get("email")
        code = random_code()
        c = Valid_Code()
        c.code_user = email
        c.code_content = code
        c.save()
        send_data = "%s的验证码为%s,打死也不要告诉别人哟" % (email, code)

        mailsend = MailSender(sender="15037609692@163.com",recever=email,password="l123456",content=send_data,subject="验证码")
        mailsend.send()

        result["data"] = "发送成功"
    else:
        result["code"] = 400
        result["data"] = "请求姿势不太对哟"
    return JsonResponse(result)


from CeleryTask.tasks import add


def get_task(request):
    num1 = request.GET.get("num1",1)
    num2 = request.GET.get("num2",2)
    add.delay(int(num1),int(num2))

    return JsonResponse({"data":"success"})


# def middle_test_view(request):
#     print("我是view")
#     return JsonResponse({"data":"hello"})

def middle_test_view(request):
    def hello():
       return HttpResponse("hello world")
    rep = HttpResponse("nihao")
    rep.render = hello
    return rep