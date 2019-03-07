from bs4 import BeautifulSoup

html = open('../html5/4.2.4.1.html', 'r', encoding='utf-8')

soup = BeautifulSoup(html, 'lxml')
# 返回是字典形式
print(soup.p.attrs)
# 返回的是str
print(soup.p.attrs['name'])
# 也是获取属性,返回str
print(soup.p['name'])
# 返回列表
print(soup.p['class'])
