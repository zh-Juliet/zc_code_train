#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/23 16:56
@Author: ZhangQiang
'''

import requests
from lxml import etree

# 需要请求的网站(搜狗热搜)
parse_url = "http://top.sogou.com/hot/shishi_1.html"

# 1. 发送请求,获取响应
res = requests.get(url=parse_url)
text = res.content.decode()
# print(text)

# 2.数据解析
html = etree.HTML(text)
li_tag_list = html.xpath("//ul[@class='pub-list']/li")
print(len(li_tag_list))

for li_tag in li_tag_list:
    topic_name = li_tag.xpath("./span[@class='s2']/p/a/text()")[0]
    print(topic_name)






