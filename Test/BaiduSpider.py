#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : BaiduSpider.py
@Author: Wesley
@Date  : 2018/11/22 17:30
@Desc  : 
'''
import requests
import re

respose = requests.get('http://www.xiaohuar.com/v/')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
urls = re.findall(r'class="items".*?href="(.*?)"', respose.text, re.S)
for url in urls:
    print(url)
