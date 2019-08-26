import re

string = "hello\tworld \n I am xiaoming this is 2019-0992_time_"

# result = re.findall(r"h",string)
# print(result)
# . 匹配非换行的任意字符
# result = re.findall(r"..",string)
# print(result)
# \w 匹配所有数字，字母下划线
# result = re.findall(r"\w\w",string)
# print(result)
# \W 匹配非\w 字符
# result = re.findall(r"\W",string)
# print(result)
# \d  匹配数字
# result = re.findall(r"\d\d",string)
# print(result)
# \D 匹配非数字
# result = re.findall(r"\D",string)
# print(result)
# [] 匹配当中的任意一个字符
# result = re.findall(r"[abhwo]",string)
# print(result)
# result = re.findall(r"[a-zA-Z0-9]",string)
# print(result)
# ^ 匹配非[]中的内容
# result = re.findall(r"[^a-zA-Z]",string)
# print(result)
# |匹配两边的字符
# result = re.findall(r"he|ll|xi|ao|ming",string)
# print(result)
# ()分组匹配 组外的作为条件
string = "201 983 686 838 636 909"
# result = re.findall(r"(\d)\d",string)
# print(result)

result = re.findall("(\d)\d",string)
print(result)

result = re.findall(r"(?P<id>\d)\d(?P=id)",string)
print(result)

s = '<a>wahaha</a>'
pattern = '<(?P<tab>\w+)>(\w+)</(?P=tab)>' #要求使用这个名字的分组和前面同名分组中的内容匹配的必须一致
ret = re.search(pattern,s)
print(ret.group(2))

s = '<h1>hello</h1>'
ret = re.findall('<(\w+)>',s)#方法1
print(ret)
#-------------------------------------------
ret = re.search('<(?P<name>\w+)>(\w+)</((?P=name))>',s)#方法2
#利用指定命名来取值

print(ret.group(1))
print(ret.group(2))
print(ret.group(3))

# dict = json.loads(resu)
# print(type(dict))
# print(dict)
li = [('mts', '1503760'), ('province', '河南'), ('catName', '中国移动'), ('telString', '15037609022'), ('areaVid', '30500'), ('ispVid', '3236139'), ('carrier', '河南移动')]
for k,v in li:
    print(k,v)
