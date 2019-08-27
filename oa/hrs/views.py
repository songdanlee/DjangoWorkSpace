from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from io import  StringIO
from django.shortcuts import render

from django.template.loader import get_template

depts_list = [
    {'no': 10, 'name': '财务部', 'location': '北京'},
    {'no': 20, 'name': '研发部', 'location': '成都'},
    {'no': 30, 'name': '销售部', 'location': '上海'},
]

# def index(request):
#     output = StringIO()
#     output.write('<html>\n')
#     output.write('<head>\n')
#     output.write('\t<meta charset="utf-8">\n')
#     output.write('\t<title>首页</title>')
#     output.write('</head>\n')
#     output.write('<body>\n')
#     output.write('\t<h1>部门信息</h1>\n')
#     output.write('\t<hr>\n')
#     output.write('\t<table>\n')
#     output.write('\t\t<tr>\n')
#     output.write('\t\t\t<th width=120>部门编号</th>\n')
#     output.write('\t\t\t<th width=180>部门名称</th>\n')
#     output.write('\t\t\t<th width=180>所在地</th>\n')
#     output.write('\t\t</tr>\n')
#     for dept in depts_list:
#         output.write('\t\t<tr>\n')
#         output.write('\t\t\t<td align=center>{no}</td>\n'.format(no=dept["no"]))
#         output.write('\t\t\t<td align=center>{name}</td>\n'.format(name=dept["name"]))
#         output.write('\t\t\t<td align=center>{dept}</td>\n'.format(dept=dept["location"]))
#         output.write('\t\t</tr>\n')
#     output.write('\t</table>\n')
#     output.write('</body>\n')
#     output.write('</html>\n')
#     return HttpResponse(output.getvalue())

def index(request):
    template = get_template("index.html")
    result = template.render({"depts_list":depts_list})
    return  HttpResponse(result)
    # 以上代码等价于以下
    # return render(request,"index.html",{"depts_list":depts_list})
