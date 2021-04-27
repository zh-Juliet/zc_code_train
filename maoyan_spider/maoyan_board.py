#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/23 14:44
@Author: ZhangQiang
'''

import json
import requests
from lxml import etree

# 请求的url
board_url = "https://maoyan.com/board"

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Cookie': 'uuid=C22881A0A3FD11EBB0D27D75E4A6B7539BBF43CA3AFE4F72A93CF2C27E185ACD;'
}

# 发送请求，获取响应
res = requests.get(url=board_url,headers=headers)
text = res.content.decode()

# print(text)

# 数据解析
html = etree.HTML(text)

dd_tag_list = html.xpath("//div[@class='main']/dl[@class='board-wrapper']/dd")
print(len(dd_tag_list))


# 遍历
for dd_tag in dd_tag_list:
    # 创建一个字典，保存数据
    item = {}

    # 电影名称
    file_name = dd_tag.xpath(".//div[@class='movie-item-info']/p[@class='name']/a/text()")[0]
    print(file_name)
    item["file_name"] = file_name

    # 主演
    star = dd_tag.xpath(".//div[@class='movie-item-info']/p[@class='star']/text()")[0]
    # print(star)   # 数据两边有空格，需要去掉

    star = star.strip()
    print(star)
    item["star"] = star

    # 上映时间
    releasetime = dd_tag.xpath(".//div[@class='movie-item-info']/p[@class='releasetime']/text()")[0]
    print(releasetime)
    item["releasetime"] = releasetime


    # 评分
    score = dd_tag.xpath(".//div[@class='movie-item-number score-num']/p[@class='score']/i/text()")
    score = "".join(score)
    print(score)
    item["score"] = score

    print(item)

    # 数据保存
    with open("./film_board.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(item,ensure_ascii=False))
        f.write("\n")

    # break







