#!/usr/bin/env python
# coding: utf-8

# ### 爬虫部分

#草稿

import requests#爬虫的库
import re#处理数据的正则库
from bs4 import BeautifulSoup#解析请求体的库

#设置请求头
h={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'cookie': 'global_cookie=fh5nib311xjyed2y4xob49ccq1ykisg4et8; engine_source_cookie=baidu; sf_source=baidu; __utma=147393320.428339446.1608185499.1608185499.1608185499.1; __utmc=147393320; __utmz=147393320.1608185499.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; city=sy; csrfToken=9-hdgLArK7gO1NWr1F3ChQWe; lastscanpage=0; g_sourcepage=esf_fy%5Elb_pc; unique_cookie=U_fh5nib311xjyed2y4xob49ccq1ykisg4et8*13; __utmb=147393320.33.10.1608185499'}

#访问一页
res=requests.get('https://sy.esf.fang.com/house/i32/?rfss=1-1b151535c40ac00312-06',headers=h)

#请求体
print(res.text)

#解析请求体
s=BeautifulSoup(res.text,'lxml')

#名字
[re.sub('\s','',j) for j in [i.text for i in s.find_all(name='span',class_='tit_shop')]]#re.sub的作用是去除其中的字段的空格部分

#详细信息
[re.sub('\s','',j) for j in [i.text for i in s.find_all(name='p',class_='tel_shop')]]

#价格
[i.b.text for i in s.find_all(name='span',class_='red')]










