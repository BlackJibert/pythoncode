from bs4 import BeautifulSoup

html = open('../html5/4.2.4.3.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
# 查询的时候是attrs参数，参数的类型是字典类型
print(soup.find_all(attrs={"id": 'list-1'}))
print(soup.find_all(attrs={"name": 'elements'}))
print('---------------------')
# 对于一些常用的属性，比如id和class等，我们可以不用attrs来传递
print(soup.find_all(id='list-1'))
# class在python是一个关键字，所以后面要加一个下划线，class_
print(soup.find_all(class_='element'))
