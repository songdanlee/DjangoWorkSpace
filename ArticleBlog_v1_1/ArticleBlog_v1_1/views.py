import hashlib

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from Article.models import *
from Article.register import Register

def set_page(page_list,page):
    """
    page_list  # 页码范围
    page #页码
    想要当前页码的前两页和后两页
    """
    if page - 3 < 0:
        start = 0
    else:
        start = page - 3
    if page+2 > 49:
        end = 49
    else:
        end = page+2
    return list(page_list[start:end])


def newList(request,types,p):
    """
    :param request:
    :param types: 文章类型
    :param p: 页码
    :return: 对应类型，对应页码的文章列表
    """
    p = int(p)

    page_size = 6
    # print(type(types),types,p)
    articles = ArticleType.objects.get(label=types).article_set.order_by("-public_time")
    # articles = ArticleType.objects.get(label="个人日记").article_set.order_by("-public_time")

    article_list = Paginator(articles,page_size) # 进行分页
    page_article = article_list.page(p) # 返回对应页码
    page_range = set_page(article_list.page_range,p)
    # article_list.num_pages 总页码数，article_list.page_range 下标从 1 开始的页数范围迭代器，article_list.count表示所有页面的对象总数
    # print(article_list.num_pages,article_list.page_range,article_list.count)
    return render(request,"newlist.html",locals())


def index(request):
    """
    :param request:
    :return:  new_article 最新的6条文章; recomm_article推荐的前8条数据；click_artcle 点击最高的前8条数据
    """
    new_article = Article.objects.order_by("-public_time")[:6]
    recomm_article = Article.objects.filter(recomment=1).order_by("-public_time")[:8]
    click_artcle = Article.objects.order_by("-click")[:8]
    username="songdan_lee"
    return render(request,"index.html", locals())


def content(request,id): # 根据id 获取文章
    article = Article.objects.get(id=id)
    return render(request,"content.html", locals())


def about(request): # 个人简介
    return render(request,"about.html")


def img(request):  # 展示图片页面
    return render(request, 'img.html')


def getImgs(request): # 瀑布流 ajax 获取图片
    nid = request.GET.get('nid')
    # nid 第一次取为 0，每次取 7 条
    last_position_id = int(nid) + 7
    postion_id = str(last_position_id)
    # 获取 0 < id < 7 的数据
    img_list = Img.objects.filter(id__gt=nid, id__lt=postion_id).values('id', 'title', 'src')
    img_list = list(img_list)   # 将字典格式转换为列表形式
    ret = {
        'status': True,
        'data': img_list
    }
    return JsonResponse(ret)


def listpic(request): # 图片页
    return render(request,"listpic.html",locals())


def request_method(request): # 查看request 的方法
    request_method = request.__dir__()
    req_arg = request.META.items()
    return render(request,"request_method.html",locals())


# def form_get(request): # 首页get 表单搜索文章
#
#     value = request.GET.get("keyboard")
#
#     search_list = []
#     if value:
#         search_list = Article.objects.filter(title__contains=value)
#     return render("search_list.html",locals())


def form_post(request): # 首页post 表单搜索文章
    value = request.POST.get("keyboard")
    search_list = []
    if value:
        search_list = Article.objects.filter(title__contains=value)
    return render(request,"search_list.html",locals())


def setPassword(password): # 加密
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def check_eamil_exists(email):
    """
    :param email:
    :return:  1 email 存在， 0 email 不存在
    """
    return 1 if User.objects.filter(email=email).first() else 0


def register(request): # 注册
    register_form = Register()

    if request.method == "POST":

        data_valid = Register(request.POST)

        if data_valid.is_valid():
            clean_data = data_valid.cleaned_data
            username = clean_data.get("username")
            email = clean_data.get("email")
            password = clean_data.get("password")
            d_password = clean_data.get("d_password")
            if check_eamil_exists(email) == 1: # 邮箱存在
                data_valid.add_error("email", "邮箱已经存在")

            elif password == d_password: # 密码一致
                user = User()
                user.username = username
                user.password = setPassword(password)
                user.email = email
                user.save()
                flag = 1
            else: # 密码不一致
                data_valid.add_error("password","两次密码不一致")

    return render(request,"register.html",locals())


def jq_exam(request):
    return render(request,"jq_example.html")


from django.http import JsonResponse


def ajax_get_page(request):
    return JsonResponse({'hello': 'world'})


def jq_post_exam(request): #post 页面
    return render(request,"jq_post_example.html")


def ajax_post_page(request): # ajax post 提交 视图
    name = request.POST.get("name")
    print(name)
    return JsonResponse({"name":name})

def register_check(request): # 检测邮箱
    email = request.GET.get("email")
    sendData = {'code':400,'data':''}
    if email:
        flag = check_eamil_exists(email)
        if flag == 1:
            sendData['data'] = '邮箱已经存在'
        else:
            sendData['code'] = 200
            sendData['data'] = '邮箱可以使用'
    else:
        sendData['data'] = '邮箱为空'
    return JsonResponse(sendData)

def check_pass(email,password,d_password): # 登录校验
    user = User.objects.filter(email=email).first()
    if user:
        db_password = user.password
        if password != d_password:
            return 3
        if password == d_password and setPassword(password) == db_password:
            return 1
        if password != db_password:
            return 2
    return 0


from django.http import HttpResponseRedirect


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        d_password = request.POST.get("d_password")
        if email and password and d_password:
            flag = check_pass(email,password,d_password)
            if flag == 1:
                response = HttpResponseRedirect("/index/") # 重定向
                response.set_cookie("name","songdan")
                return response
            else:
                return render(request, "login.html",{'flag':flag})
    return render(request, "login.html")


def login_check(request):
    sendData = {'code': 400, 'data': ''}
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            if check_eamil_exists(email) == 1:
                sendData['code'] = 200
                sendData['data'] = '提交成功'
            else:
                sendData['data'] = '邮箱未注册账号'
    print(sendData)
    return JsonResponse(sendData)

