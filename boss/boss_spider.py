#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/25 11:11
@Author: ZhangQiang
'''


import time
from selenium import webdriver
from lxml import etree


# 创建dirver对象
driver = webdriver.Chrome()

# 发送请求
driver.get("https://www.zhipin.com/beijing/")

# 最大化浏览器界面
driver.set_window_size(1920,1080)

# 定位搜索框,输入需要查找的岗位
driver.find_element_by_xpath("//div[@class='search-form-con']/p[@class='ipt-wrap']/input").send_keys("翻译")

# 点击搜索
driver.find_element_by_xpath("//button[@class='btn btn-search']").click()

# 等待2s,让浏览器完全加载出来页面内容
time.sleep(2)

# 获取网页内容
text = driver.page_source

# 解析html,获取岗位信息
html = etree.HTML(text)
li_tag_list = html.xpath("//div[@class='job-list']/ul//li")
print("当前页面岗位个数：{}".format(len(li_tag_list)))

for li_tag in li_tag_list:
    item = {}

    # 岗位名称
    item["position_name"] = li_tag.xpath(".//span[@class='job-name']/a/text()")[0]

    # 公司
    item["company"] = li_tag.xpath(".//div[@class='info-company']/div/h3/a/text()")[0]

    # 工作地址
    item["address"] = li_tag.xpath(".//span[@class='job-area']/text()")[0]

    # 薪酬
    item["salary"] = li_tag.xpath("//div[@class='job-limit clearfix']/span[@class='red']/text()")[0]

    # 工作经验
    item["experience"] = li_tag.xpath("//div[@class='job-limit clearfix']/p/text()")[0]

    # 学历
    item["education"] = li_tag.xpath("//div[@class='job-limit clearfix']/p/text()")[1]

    print(item)


time.sleep(2)
# 翻页
driver.find_element_by_xpath("//div[@class='page']/a[@class='next']").click()

# 退出driver
driver.quit()
