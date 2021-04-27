#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/25 15:27
@Author: ZhangQiang
'''

import json
import requests
from  urllib.parse import urlencode
from lxml import etree


class MaoYanSpider(object):
    '''猫眼电影'''

    def __init__(self,showType,catId,sourceId,yearId):
        self.base_url = "https://maoyan.com/films?"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'Cookie': 'uuid=C22881A0A3FD11EBB0D27D75E4A6B7539BBF43CA3AFE4F72A93CF2C27E185ACD;'
        }
        self.showType = showType
        self.catId = catId
        self.sourceId = sourceId
        self.yearId = yearId


    def get_page_url(self):
        '''构造url'''

        # 构造参数
        data = {
            "showType": self.showType,
            "catId": self.catId,
            "sourceId": self.sourceId,
            "yearId": self.yearId
        }

        # 构造url
        parse_url = self.base_url + urlencode(data)
        print(parse_url)
        return parse_url

    def parse_film_page(self,parse_url):
        '''发送请求，获取响应'''

        res = requests.get(url=parse_url, headers=self.headers)
        text = res.content.decode()

        html = etree.HTML(text)
        dd_tag_list = html.xpath("//dl[@class='movie-list']//dd")

        print("符合条件的电影个数：{}".format(len(dd_tag_list)))

        if len(dd_tag_list) > 0:
            for dd_tag in dd_tag_list:
                item = {}
                # 电影名称
                file_name = dd_tag.xpath("./div[@class='movie-item film-channel']//div[@class='movie-hover-info']/div[1]/span/text()")[0]

                # print(file_name)
                item["file_name"] = file_name

                file_type = dd_tag.xpath("./div[@class='movie-item film-channel']//div[@class='movie-hover-info']/div[2]/text()")

                file_type = ("".join(file_type)).strip()
                # print(file_type)
                item["file_type"] = file_type

                # 主演
                star = dd_tag.xpath(
                    "./div[@class='movie-item film-channel']//div[@class='movie-hover-info']/div[3]/text()")
                star = ("".join(star)).strip()
                # print(star)   # 数据两边有空格，需要去掉
                item["star"] = star

                # 上映时间
                releasetime = dd_tag.xpath(
                    "./div[@class='movie-item film-channel']//div[@class='movie-hover-info']/div[4]/text()")
                releasetime = ("".join(releasetime)).strip()
                # print(releasetime)
                item["releasetime"] = releasetime

                # 评分
                score = dd_tag.xpath("./div[@class='channel-detail channel-detail-orange']//text()")
                score = "".join(score)
                # print(score)
                item["score"] = score

                print(item)
                # 数据保存
                with open("./film_data.txt", "a", encoding="utf-8") as f:
                    f.write(json.dumps(item, ensure_ascii=False))
                    f.write("\n")



    def run(self):
        # 1.构造url
        parse_url = self.get_page_url()

        # 2.获取数据
        item = self.parse_film_page(parse_url)


if __name__ == '__main__':
    showType = input('请输入你要搜索的电影类型("正在热映":1,"即将上映":2,"经典影片":3): ')
    # print(showType)

    catId = input('请输入你要搜索的电影风格("爱情":3,"喜剧":2,"动画":4,"剧情"：1): ')
    # print(catId)

    sourceId = input('请输入你要搜索的电影区域("大陆":2,"美国":3,"韩国":7,"日本":6): ')

    yearId = input('请输入你要搜索的电影年代("2021":16,"2020":15,"2019":14): ')
    # print(yearId)

    # 获取电影数据
    maoyanspider = MaoYanSpider(showType, catId, sourceId, yearId)
    maoyanspider.run()
