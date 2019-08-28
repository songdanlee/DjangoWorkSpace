from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response


def newList(request):
    tempalte = get_template("newlist.html")
    result = tempalte.render({})

    return HttpResponse(result)

def index(request):

    return render_to_response("index.html",{"username":"songdan"})

def new(request):

    return render_to_response("about.html")

def listpic(request):
    return render_to_response("listpic.html")