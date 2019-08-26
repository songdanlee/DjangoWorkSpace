from django.http import HttpResponse
import time
import requests
import re


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
