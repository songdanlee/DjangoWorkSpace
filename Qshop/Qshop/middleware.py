from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from Qshop.settings import ERROR_PATH
import time


class MiddleWareTest(MiddlewareMixin):


    def process_request(self,request):
        ip = request.META.get("REMOTE_ADDR")
        print("我是process_request1")
        if ip == "10.10.14.167":
            return HttpResponse("<h1>非法ip</h1>")



    def process_view(self,request,callback,callback_args,callback_kwargs):
        """
        :param request:请求
        :param callback: 对应视图函数,访问那个视图就是那个视图
        :param callback_args: 视图函数对应的参数 元组类型
        :param callback_kwargs: 视图函数的参数， 字典类型
        :return:
        """
        print("我是process_view1")
        print(callback)

    def process_exception(self,request,exception):
        """
        出现异常执行
        :param excetion:
        :return:
        """
        if exception:
            with open(ERROR_PATH,"a") as f:
                now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                content = "[%s]:%s\n"%(now,exception)
                f.write(content)
                # 发送邮件
            return HttpResponse("代码出错了%s"%exception)


    def process_template_response(self,request,response):
        """
        必须返回一个render才可以触发
        :param request:
        :param response:
        :return:
        """
        print("我是process_template_response1")
        return HttpResponse("123")


    def process_response(self,request,response):
        """
        process_response 和 process_template_response必须有返回值
        :param request:
        :param response:
        :return:
        """
        print("我是process_response1")
        return response


class middleware2(MiddlewareMixin):

    def process_request(self,request):
        print("process_request2")
        print(request.META.get("REMOTE_ADDR"))

    def process_views(self,request,callback,callback_args,callback_kwargs):
        print("process_views2")
        print(callback)

    def process_exception(self,request,exception):

        if exception:
            print("%s"%exception)
            return HttpResponse("%s"%exception)
    def process_response(self,request,response):
        print("process_response2")
        return response