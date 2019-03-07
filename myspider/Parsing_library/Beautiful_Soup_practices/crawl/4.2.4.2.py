from bs4 import BeautifulSoup

html = open('../html5/4.2.4.1.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
# Tag类型
print(type(soup.title))
print(soup.title.string)
print(soup.title.name)
print(soup.head)
# 结果是第一个p节点的内容
print(soup.p)
