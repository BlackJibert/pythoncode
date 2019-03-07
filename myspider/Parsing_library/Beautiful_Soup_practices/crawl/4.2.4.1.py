# 4.2.4.1.py
from bs4 import BeautifulSoup

#
# html = etree.parse("../html5/4.2.4.1.html", etree.HTMLParser())
# 解析本地一个html文件
html = open("../html5/4.2.4.1.html", 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
# 调用prettify()方法，这个方法以标准的缩进格式输出
print(soup.prettify())
# print(soup.title)
print(soup.title.string)
