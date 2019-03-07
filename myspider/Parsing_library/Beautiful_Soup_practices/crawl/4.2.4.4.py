from bs4 import BeautifulSoup

html = open('../html5/4.2.4.1.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)
