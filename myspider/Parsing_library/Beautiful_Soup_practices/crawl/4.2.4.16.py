from bs4 import BeautifulSoup

html = open('../html5/4.2.4.3.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('Get_Text:', li.get_text())
    print('String:', li.string)
