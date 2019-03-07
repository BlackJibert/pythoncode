from bs4 import BeautifulSoup

html = open('../html5/4.2.4.3.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
print(type(soup.find(name='ul')))
# 还是注意这里name是节点的名称
print(soup.find(name='ul'))
print(soup.find(name='li'))
print(soup.find(class_='list'))
