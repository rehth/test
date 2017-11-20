import re
"""
单个字符匹配
    .	匹配任意1个字符（除了\n）
    [ ]	匹配[ ]中列举的字符
    \d	匹配数字，即0-9
    \D	匹配非数字，即不是数字
    \s	匹配空白，即 空格，tab键
    \S	匹配非空白
    \w	匹配单词字符，即a-z、A-Z、0-9、_、汉字
    \W	匹配非单词字符
"""
#   .	匹配任意1个字符（除了\n）
match_obj = re.match(".{3}", "xHe_34 哈哈")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#  [ ]	匹配[ ]中列举的字符
match_obj = re.match("[a-zA-Z_]{4}[.]\..{2}", "xHe_..34 哈哈")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#  \d  匹配数字，即0-9    \D	匹配非数字，即不是数字
match_obj = re.match("[a-zA-Z_]{4}\d{2}\D", "xHe_34 哈哈")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#   \s	匹配空白，即 空格，tab键
match_obj = re.match("[a-zA-Z_]{4}\d\s\d", "xHe_3\t4 哈哈")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#   \w	匹配单词字符，即a-z、A-Z、0-9、_、汉字
match_obj = re.match("[a-zA-Z_]{4}\d\s\d\s\w{5}", "xHe_3\t4 aD5哈哈")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")