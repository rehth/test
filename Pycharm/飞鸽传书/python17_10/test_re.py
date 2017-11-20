import re

s = "zhangqianjun"

res = re.match("zhang", s)

print(res.group())

# 没有找到会报错
# AttributeError: 'NoneType' object has no attribute 'group'
result = re.match("[1-9]\d.\D\S\w", "14dsfsdf")     # 14dsfs
print(result.group())