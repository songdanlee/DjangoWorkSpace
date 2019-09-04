import hashlib

from django.shortcuts import render,HttpResponseRedirect
from LoginUser.models import *


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
        if email:  # 邮箱不为空
            user = LoginUser.objects.filter(email=email).first()  # 查找邮箱是否注册
            if not user:  # 未注册
                if password:  # 密码不为空
                   loginuser = LoginUser()
                   loginuser.username = email
                   loginuser.email = email
                   loginuser.password = getPassword(password) # 加密数据
                   loginuser.save() # 保存到数据库
                   successmsg = "恭喜你注册成功"
                else:
                    errormsg = "密码为空"
            else:
                errormsg = "邮箱已被注册"
        else:
            errormsg = "邮箱为空"

    return render(request,"register.html",locals()) # 未成功，返回错误信息


def loginValid(func):
    """
    :desc 闭包函数校验是否登录
    :param func:
    :return:
    """
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get("username")
        id = request.COOKIES.get("id")
        session_username = request.session.get("session_username")
        if username and id:
            user = LoginUser.objects.filter(id=id).first()
            if user.username == username:
                return func(request, *args, **kwargs)
        return HttpResponseRedirect("/login/")
    return inner


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
        if email:  # 邮箱不为空
            user = LoginUser.objects.filter(email=email).first()
            if user:  # 数据库可以查找到用户
                if password:  # 密码不为空
                    db_password = user.password  # 数据库中用户的密码
                    password = getPassword(password)  # 输入密码加密
                    if password == db_password:  # 密码正确,登录成功
                        response = HttpResponseRedirect("/index/")
                        response.set_cookie("username",user.username) # 添加cookie
                        response.set_cookie("id",user.id)
                        request.session['session_username'] = user.username # 添加session
                        return response# 跳转到index首页
                    else:
                        errormsg = "密码不正确"
                else:
                    errormsg = "密码为空"
            else:
                errormsg = "邮箱未注册"
        else:
            errormsg = "邮箱为空"

    return render(request,"login.html",locals())


@loginValid
def index(request):
    """
    :desc 返回index页面
    :param request:
    :return:
    """
    return render(request,"index.html",locals())


def logout(request):
    """
    :desc 退出登录
    :param request:
    :return:
    """
    response = HttpResponseRedirect("/login/")
    cookies = request.COOKIES
    print("清除cookie开始")
    for cookie in cookies.keys():
        print(cookie)
        response.delete_cookie(cookie)
    print("清除cookie结束")
    if request.session.get('session_username'):
        del request.session['session_username']
    return response



