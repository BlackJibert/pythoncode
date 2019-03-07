import re

from bs4 import BeautifulSoup

html = open('../html5/4.2.4.4.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
# 我们在find_all()方法中传入text参数，该参数为正则表达式，返回为符合对象的节点文本组成的列表
print(soup.find_all(text=re.compile('link')))
