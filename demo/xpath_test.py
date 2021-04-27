#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/27 14:38
@Author: ZhangQiang
'''

# 导入lxml库
from lxml import etree

text = ''' <div> 
            <ul> 
            <li class="item-1"><a>first item</a></li> 
            <li class="item-2"><a href="link2.html">second item</a></li> 
            <li class="item-3"><a href="link3.html">third item</a></li> 
            <li class="item-4"><a href="link4.html">fourth item</a></li> 
            <li class="item-5"><a href="link5.html">fifth item</a> 
            </ul> 
            <p> 我来自中国传媒大学</p>
            </div> 
        '''

# Element对象，Element对象才能使用xpath方法
html = etree.HTML(text)
print(html)


result1 = html.xpath("//li[@class='item-1']/a/text()")
print(result1)

result2 = html.xpath("//li[@class='item-2']/a/@href")
print(result2)


result3 = html.xpath("//div/p/text()")
print(result3)

