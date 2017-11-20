import re

r"""
分组:
    |	匹配左右任意一个表达式
    (ab)	将括号中字符作为一个分组
    \num	引用分组num匹配到的字符串
    (?P<name>)	分组起别名
    (?P=name)	引用别名为name分组匹配到的字符串
"""
# match 匹配表示就是从开头匹配
str_list = ["hello", "world", "python", "java"]
mystr = "hello world python java"
match_obj = re.match("(hello)|(world)", mystr)
if match_obj:
    print(match_obj.group(1))   # hello
    print(match_obj.group(2))   # None
else:
    print("匹配失败")


s = "<html>hh</html>"
match_obj = re.match("<(?P<name1>[a-zA-Z]+)>.*</(?P=name1)>", s)
if match_obj:
    print(match_obj.group(1))   # html 这里就一个分组
    print(match_obj.group())    # <html>hh</html>
    # print(match_obj.group(2))
else:
    print("匹配失败")


# re.search() 查找
search_obj = re.search("\d+", "我花了532块钱")
if search_obj:
    print(search_obj.group())   # 532
else:
    print("匹配失败")


# re.findall() 查找所有,会返回一个列表
find_list = re.findall("[0-9]+|\d+", "ds23dsf654sdf3214")
print(find_list)    # ['23', '654', '3214']


# re.sub()　替换
def tt(sub_obj):
    a = sub_obj.group()
    return str(ord(a))
sub_str = re.sub("f", tt, "s f s")
print(sub_str)  # "s 102 s"


# 贪婪: (python默认贪婪)尝试匹配尽可能多的字符
sss = "this is number 223-331-3123-2353"
search_obj = re.search(".*(\d+-\d+-\d+-\d+)", sss)
if search_obj:
    print(search_obj.group(1))  # 3-331-3123-2353
else:
    print("匹配失败")

# 非贪婪: (可用 ? 改为非贪婪)尝试匹配尽可能少的字符
search_obj = re.search(".*?(\d+-\d+-\d+-\d+)", sss)
if search_obj:
    print(search_obj.group(1))  # 223-331-3123-2353
else:
    print("匹配失败")

# Python中字符串前面加上 r 表示原生字符串
# 正则表达式里使用"\"作为转义字符
# r 的作用:　字符转义
sss = "c:\\user\\king\\Desktop\\"

search_obj = re.search(r".*\\.*\\.*\\.*\\", sss)
if search_obj:
    print(search_obj.group())   # c:\user\king\Desktop\
else:
    print("匹配失败")