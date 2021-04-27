#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/27 15:10
@Author: ZhangQiang
'''

import re

str_text = "中国传媒大学创建于1954年"

result = re.findall(r"\d+",str_text)
print(result)

result2 = re.search(r"(.*?)创",str_text).group(1)
print(result2)

# 其他方法
# re.search()
# re.match()
# re.sub()
# re.compile()

# 规则：
# \d 匹配一个数字  \D 匹配非数字
# \s 匹配空白字符(\r\n空格等)  \S 匹配非空白字符
# \w 匹配单词字符(a-zA-Z_)  \W 匹配非单词字符

# .匹配任意字符
# *匹配前一个字符0次或者无限次
# + 匹配前一个字符1次或无限次
# ？ 匹配前一个字符0次或1次

