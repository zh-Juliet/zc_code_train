#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/25 15:53
@Author: ZhangQiang
'''

import re
import requests
from lxml import etree


class CucNewsSpdier(object):

    def __init__(self):
        self.base_url = "http://www.cuc.edu.cn/"
        self.url = "http://www.cuc.edu.cn/news/1901/list.htm"

    def parse_url(self,url):
        '''发送请求，获取响应'''
        res = requests.get(url)
        return res.content.decode()

    def get_detail_page_url(self):
        '''获取所有详情页url'''
        detail_url_list = []
        text = self.parse_url(self.url)
        html = etree.HTML(text)

        ul_tag_list = html.xpath("//div[@class='bd']/ul")
        print(len(ul_tag_list))

        for ul_tag in ul_tag_list:
            news_title = ul_tag.xpath("./li[@class='g-lastu']/h3/a/text()")[0]
            news_detail_url = ul_tag.xpath("./li[@class='g-lastu']/h3/a/@href")[0]
            print(news_title, news_detail_url)
            news_detail_url = self.base_url + news_detail_url
            detail_url_list.append(news_detail_url)
            break
        return detail_url_list


    def parse_detail_page(self,url):
        '''获取详情页内容'''

        # 发送详情页的请求，获取网页数据
        text = self.parse_url(url)

        # 将网页字符串转化成html对象
        html = etree.HTML(text)

        # 创建字典储存数据
        item = {}

        # 新闻来源
        source_text = html.xpath("//span[@class='arti-name']/text()")[0]
        source = re.search(r".*?来源：(.*?)\r\n", source_text).group(1)
        item["source"] = source

        # 标题
        title = html.xpath("//figure[@class='tit-area']/h1/text()")[0]
        item["title"] = title

        # 发布时间
        pub_time = re.search(r".*?(\d+-\d+-\d+)\r\n", source_text).group(1)
        item["pub_time"] = pub_time

        # 浏览量(和页面展示的浏览量不一致)
        visit_count = html.xpath("//span[@id='hits']/span/text()")[0]
        item["visit_count"] = visit_count

        # 编辑
        author_text = html.xpath("//article[@class='con-area']/div/p[last()]/text()")[0]
        author = re.search(r"（编辑(.*?)）", author_text).group(1)
        author = re.sub(r"：|\s","",author)
        item["author"] = author

        # 新闻网址
        item["detail_page_url"] = url

        # 内容
        content = html.xpath("//article[@class='con-area']/div[@class='wp_articlecontent']/p//text()")
        content = "".join(content)
        item["content"] = content
        print(item)


    def run(self):
        '''主函数'''

        # 1.发送中传要闻主页请求，获取详情页url
        detail_url_list = self.get_detail_page_url()

        # 2.遍历详情页网址，获取每一条新闻的数据
        for detail_url in detail_url_list:
            self.parse_detail_page(detail_url)


if __name__ == '__main__':
    cucnewsspider = CucNewsSpdier()
    cucnewsspider.run()


