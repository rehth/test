import re
"""
多字符：
    *	匹配前一个字符出现0次或者无限次，即可有可无
    +	匹配前一个字符出现1次或者无限次，即至少有1次
    ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
    {m}	匹配前一个字符出现m次
    {m,n}	匹配前一个字符出现从m到n次
    ^	匹配字符串开头
    $	匹配字符串结尾
"""
# [^sss] 除了sss 都匹配
match_obj = re.match("^[0-9].*[^5]$", "3hello5")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# 匹配微博话题
search_obj = re.search("#[^#]+[#]", "gdfgdfg#dgdfgg#gfdgf#hrtfthf")
if search_obj:
    print(search_obj.group())
else:
    print("匹配失败")

# 匹配手机号 排除４, 7结尾
match_obj = re.match("^1[345789][1-9]{8}[0-35-68-9]$", "13545463423")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# 匹配邮箱
match_obj = re.match("[a-zA-Z0-9]{4,20}@(163|126|qq|sina|foxmail)\.com$", "222222@qq.com")
if match_obj:
    print(match_obj.group())
    print(match_obj.group(1))
else:
    print("匹配失败")

# 匹配url开头的协议
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
url = "https:www.baidu.com"
search_obj = re.search("http[s]?:", url)
if search_obj:
    print(search_obj.group())
else:
    print("匹配失败")