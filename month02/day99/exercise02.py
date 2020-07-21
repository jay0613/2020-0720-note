"""
爬虫实例.
"""

import requests
import re
url = "https://movie.douban.com/chart"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
a = requests.get(url, headers = headers)
print(a.text)
b = a.text
c = ' <a class="nbg" href="https://movie.douban.com/subject/34961898/"  title="汉密尔顿">'
patterm = re.compile('<a.*?nbg.*?title="(.*?)">',re.S)
items = re.findall(patterm,b)
print(items)