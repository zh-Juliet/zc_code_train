#-*- coding:utf-8 -*-


'''
@Time  : 2021/4/27 14:12
@Author: ZhangQiang
'''

# 1.安装requests第三方包,导入
import requests

# 请求头
headers = {
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


# 2.发送请求，获取响应
response = requests.get("http://httpbin.org/get",headers=headers)

# 3.获取网页源代码,响应的html
print(response.content.decode())

# 请求头
print(response.request.headers)

# 4.状态码
print(response.status_code)

# 5.响应头
print(response.headers)