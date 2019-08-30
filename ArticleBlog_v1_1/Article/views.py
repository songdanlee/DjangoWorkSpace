import math

from django.shortcuts import render_to_response
from django.core.paginator import Paginator

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
    page_article = article_list.page(p) # 返回对应页
    page_range = set_page(article_list.page_range,p)

    return render_to_response("newlist.html",locals())


def index(request):
    new_article = Article.objects.order_by("-public_time")[:6]
    recomm_article = Article.objects.filter(recomment=1).order_by("-public_time")[:8]
    click_artcle = Article.objects.order_by("-click")[:8]
    return render_to_response("index.html", locals())


def content(request,id):
    article = Article.objects.get(id=id)
    print("id",article.id)
    print("title",article.title)
    print("description",article.description)
    print("content",article.content)
    print("picture",article.picture)
    return render_to_response("content.html", locals())


def listpic(request):
    return render_to_response("listpic.html")


def about(request):
    return render_to_response("about.html")

if __name__ == '__main__':
    # article_list = Article.objects.all(); # 查询所有
    # print(article_list)
    # article_list = Article.objects.filter(title="清平调") # 查询部分
    # article_list = Article.objects.filter(id=200)
    # article_list = Article.objects.order_by("-id")  # 倒序
    # article_list = Article.objects.order_by("id")  # 正序
    # print(article_list)
    pass