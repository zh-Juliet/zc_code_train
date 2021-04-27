#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/23 20:07
@Author: ZhangQiang
'''

import re
import requests
from lxml import etree


class ImageSpider(object):
    '''图片搜素'''

    def __init__(self,text):
        self.parse_url = "http://soso.nipic.com/?q={}".format(text)


    def parse_image(self):
        '''发送获取图片请求'''
        res = requests.get(url=self.parse_url)
        text = res.content.decode()
        html = etree.HTML(text)
        url_list = html.xpath("//div[@id='left-imgList-img']/ul/li[@class='new-search-works-item']/a/img/@data-original")
        print(url_list)
        print(len(url_list))
        return url_list

    def save_image(self,image_url):
        '''保存图片'''
        image_name = re.search(r".*?(\d+_\d+).jpg",image_url).group(1)
        res = requests.get(url=image_url)
        with open("./images/{}.jpg".format(image_name),"wb") as f:
            f.write(res.content)
        print("图片:{}保存成功,文件名是：{}.jpg".format(image_url,image_name))


if __name__ == '__main__':
    imagespider = ImageSpider("神州飞船")
    url_list = imagespider.parse_image()
    for i in url_list:
        imagespider.save_image(i)
        # break
