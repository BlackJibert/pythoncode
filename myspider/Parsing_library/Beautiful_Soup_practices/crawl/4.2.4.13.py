from bs4 import BeautifulSoup

html = open('../html5/4.2.4.3.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
# class属性用.,逐层深入
print(soup.select('.panel .panel-heading'))
# 也可以选择节点名
print(soup.select('ul li'))
# id属性用#
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
