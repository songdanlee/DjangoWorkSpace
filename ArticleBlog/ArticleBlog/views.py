from django.http import HttpResponse
import time
import requests
import re
from django.template.loader import get_template
from ArticleBlog.art_content import *

def index(request):
    return HttpResponse("<h1 style='color:red'>hello world</h1>")


def wel(request):
    data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(data)
    return HttpResponse("<h1 style='color:red'>当前时间为：{t}</h1>".format(t=data))


def introduce(request, name, age):
    return HttpResponse("<h1 style='color:red'>Hello,I am %s.I am %s years old</h1>" % (name, age))


def getphone(request, phone):
    data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=' + phone
    content = requests.get(url=url).text
    result = re.findall("(\w+):'([^']+)", content)

    dict = {k: v for k, v in result}
    return HttpResponse(
        "<h1 style='color:red'>当前时间为：{t}</h1><p style='color:#00FF00;font-size:20px'>{dict}</p>".format(dict=dict,
                                                                                                        t=data))

def readme(request, name):
    return HttpResponse("Welcome %s" % name)


def view_index(request):
    tempalte = get_template("index.html")
    result = tempalte.render({})
    return HttpResponse(result)


def page_list(request, page):
    page = int(page)
    tempalte = get_template("page_list.html")
    result = tempalte.render({"page": page})
    return HttpResponse(result)


def template_variable(request):
    data = {
        "name": "张三",
        "en_name": "zs",
        "project": ["python", "java", "c", "C++", "c#"],
        "score": {"python": 100, "java": 75}
    }
    template = get_template("template_variable.html")
    result = template.render(data)
    return HttpResponse(result)


def template_label(request):
    data = {
        "teacher": [{
            "name": "张三",
            "age": 14,
        },
            {
                "name": "李四",
                "age": 25,
            },
            {
                "name": "王五",
                "age": 68,
            }]
        ,
        "teacher2": [{
            "name": "张三2",
            "age": 14,
        },
            {
                "name": "李四2",
                "age": 25,
            },
            {
                "name": "王五2",
                "age": 68,
            }]
    }
    template = get_template("template_label.html")
    result = template.render(data)
    return HttpResponse(result)

articles = [
    {"id": 1, "title": "背影", "author": "朱自清", "public_time": "1925","content": beiying,"image":"image/by.jpg"},
    {"id": 2, "title": "骆驼祥子", "author": "老舍", "public_time": "1936-3-3", "content": xiangzi,"image":"image/ltxz.jpeg"},
    {"id": 3, "title": "岳阳楼记", "author": "范仲淹", "public_time": "公元1046年6月", "content": yueyanglou,"image":"image/yylj.jpg"},
    {"id": 4, "title": "滕王阁序", "author": "王勃 ", "public_time": "上元二年（675年）", "content": tengwangge,"image":"image/twgx.jpg"},
    {"id": 5, "title": "侠客行", "author": "李白", "public_time": "天宝三载（744年）", "content": xiakexing,"image":"image/xkx.jpg"}
]

def article_list(request):
    template = get_template("article_list.html")
    result = template.render({"article":articles,"aa":"abc"})
    return HttpResponse(result)

def article_content(request,id):
    id = int(id)
    article = ""
    for art in articles:
        if art.get("id")==id:
            article = art
            break;

    template = get_template("article_content.html")
    result = template.render(article)
    # result = template.render({"article":article})
    return HttpResponse(result)
