import hashlib

from django.shortcuts import render_to_response,render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template import RequestContext
from Article.models import *


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
    :return:
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
    new_article = Article.objects.order_by("-public_time")[:6]
    recomm_article = Article.objects.filter(recomment=1).order_by("-public_time")[:8]
    click_artcle = Article.objects.order_by("-click")[:8]
    username="songdan_lee"
    return render(request,"index.html", locals())


def content(request,id):
    article = Article.objects.get(id=id)
    return render(request,"content.html", locals())


def listpic(request):
    return render(request,"img.html")


def about(request):
    return render(request,"about.html")


def img(request):
    return render(request, 'img.html')


def getImgs(request):

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


def new(request):
    article = Article.objects.get(id=1)
    return render(request,"about.html", locals())


def listpic(request):
    return render(request,"listpic.html",locals())


def request_method(request):
    request_method = request.__dir__()
    req_arg = request.META.items()
    return render(request,"request_method.html",locals())


def form_get(request):

    value = request.GET.get("keyboard")

    search_list = []
    if value:
        search_list = Article.objects.filter(title__contains=value)
    return render("search_list.html",locals())


def form_post(request):
    value = request.POST.get("keyboard")
    search_list = []
    if value:
        search_list = Article.objects.filter(title__contains=value)
    return render(request,"search_list.html",locals())


def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = User()
            user.username = username
            user.password = setPassword(password)
            user.save()
    return render(request,"register.html",locals())
