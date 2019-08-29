from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Article.models import *

def newList(request):

    # article_list = Article.objects.all(); # 查询所有
    # print(article_list)
    # article_list = Article.objects.filter(title="清平调") # 查询部分
    # article_list = Article.objects.filter(id=200)
    # article_list = Article.objects.order_by("-id")  # 倒序
    article_list = Article.objects.order_by("id")# 正序
    # print(article_list)

    return render_to_response("newlist.html",locals())


def index(request):
    return render_to_response("index.html", {"username": "songdan"})


def new(request):
    article = Article.objects.get(id=1)
    return render_to_response("about.html", locals())


def listpic(request):
    return render_to_response("listpic.html")
