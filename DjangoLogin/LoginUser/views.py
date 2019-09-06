import hashlib

from django.shortcuts import render,HttpResponseRedirect,HttpResponse
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

from django.core.paginator import Paginator

@loginValid
def goods_list(request,status="up",page=1):
    page = int(page)
    if status == "down":
        goods = Goods.objects.filter(goods_status=0)
    elif status == 'up':
        goods = Goods.objects.filter(goods_status=1)
    else:
        goods = Goods.objects.all()
    goods_pagin = Paginator(goods,10)
    goods_lists = goods_pagin.page(page)
    return render(request,"goods_list.html",locals())

@loginValid
def goods_status(request,state,id):
    goods = Goods.objects.get(id=int(id))
    if state == 'up': # 上架
        goods.goods_status = 1
    elif state == 'down':
        goods.goods_status = 0
    goods.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

from django.http import JsonResponse


def goods_list_api(request,status="up",page=1):
    page = int(page)
    if status == "down":
        goods = Goods.objects.filter(goods_status=0)
        mark=0
    elif status == 'up':
        goods = Goods.objects.filter(goods_status=1)
        mark=1
    else:
        goods = Goods.objects.all()

    goods_pagin = Paginator(goods,10)
    if page in goods_pagin.page_range:
        goods_lists = goods_pagin.page(page)
    else:
        goods_lists = []
    lis = []
    for p in goods_lists:
        res = {}
        res["goods_num"] = p.goods_num
        res["id"] = p.id
        res["goods_name"] = p.goods_name
        res["goods_price"] = p.goods_price
        res["goods_count"] = p.goods_count
        res["goods_location"] = p.goods_location
        res["goods_pro_date"] = p.goods_pro_date
        res["goods_save_month"] = p.goods_save_month
        res["goods_status"] = p.goods_status
        lis.append(res)

    resu = {
        "page_range" :list(goods_pagin.page_range),
        "page":page,
        "goods_lists":lis,
        "status":mark
    }

    return JsonResponse(resu)



import random
# 添加数据
def goods_add(request):
    goods_name = "四季豆 豌豆 胡豆 毛豆 土豆 黄豆芽 绿豆芽、豆芽 甘蓝菜 包心菜 大白菜 小白菜 水白菜 西洋菜 通心菜 潺菜 花椰菜 西兰花 空心菜 金针菜 芥菜 芹菜 蒿菜 甜菜 紫菜 生菜 菠菜 韭菜 香菜 发菜 榨菜 雪里红 莴苣 芦笋 竹笋 笋干 韭黄 白萝卜 胡萝卜 荸荠 菜瓜 丝瓜 水瓜 南瓜 苦瓜 黄瓜 青瓜 付子瓜 冬瓜 小黄瓜 山芋 芋头 百叶 香菇 草菇 金针菇 蘑菇 冬菇 姬菇 萍菇 圣女小番茄 番茄 茄子 马铃薯 莲藕 木耳 白木耳 生姜 仔姜 洋姜 荞头 大蒜 蒜头 小葱 大葱 洋葱 青葱 青椒 大红椒 小红椒 红尖椒 圆椒 长茄子 太空茄子 羊肉、牛肉、猪肉、猪肠、腊肉、猪肝、牛肝、火腿、牛肚、猪肺、牛肉丸、猪脑、羊脑、五花肉 方便面、饺子、粉条、面条、碗面、河粉、米粉、粉丝、豆面、烩面、大米、小米、酸辣粉、馒头、炒面".replace(" ","、").split("、")
    goods_addr = "中牟县、兰考县、通许县、杞县、尉氏县、宜阳县、孟津县、新安县、洛宁县、栾川县、伊川县、汝阳县、嵩县、鲁山县、宝丰县、叶县、郏县、安阳县、滑县、汤阴县、内黄县、浚县、淇县、新乡县、长垣县、获嘉县、原阳县、延津县、封丘县、修武县、博爱县、武陟县、温县、濮阳县、清丰县、南乐县、台前县、范县、鄢陵县、襄城县、舞阳县、临颍县、渑池县、卢氏县、民权县、宁陵县、柘城县、虞城县、夏邑县、睢县、鹿邑县、扶沟县、西华县、商水县、沈丘县、淮阳县、郸城县、太康县、新蔡县、西平县、遂平县、平舆县、上蔡县、正阳县、泌阳县、确山县、汝南县、南召县、西峡县、方城县、镇平县、内乡县、淅川县、社旗县、唐河县、新野县、桐柏县、固始县、罗山县、光山县、潢川县、淮滨县、商城县、新县、息县".replace("县、"," ").strip().split(" ")
    goods_addr_s = [i+"县" for i in goods_addr if len(i) == 1]
    goods_addr_m = [i  for i in goods_addr if len(i) > 1]
    goods_addr = goods_addr_s + goods_addr_m

    for j,i in enumerate(range(100),1):
        good = Goods()
        good.goods_num = str(j).zfill(5)
        good.goods_name = random.choice(goods_addr) + random.choice(goods_name)
        good.goods_price = random.random()*100
        good.goods_count = random.randint(30,200)
        good.goods_location = random.choice(goods_addr)
        good.goods_save_month = random.randint(1,18)
        good.save()
    return HttpResponse("添加成功")

def goods_update(request):
    goods = Goods.objects.all()
    for good in goods:
        good.goods_num = str(good.id).zfill(5)
        good.save()
    return HttpResponse("修改成功")
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



def vue(request):
    return render(request,"vue_goods.html")


from django.views import View

class Goods(View):

    def __init__(self,**kwargs):
        super(Goods, self).__init__(**kwargs)
        self.result = {
            "code":200,
            "data":"",
        }
        self.obj = Goods



    def get(self,request):
        id = request.GET.get("id")
        if id:
            goods = self.obj.objects.get(id=id)
        else:
            goods = self.obj.objects.all()

        return JsonResponse({"method":'get',"status":1})

    def post(self,request):
        return JsonResponse({"method":'post',"status":2})

    def put(self,request):
        return JsonResponse({"method":'put',"status":3})

    def delate(self,request):
        return JsonResponse({"method":'delate',"status":4})

