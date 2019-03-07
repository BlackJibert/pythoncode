from bs4 import BeautifulSoup

html = open('../html5/4.2.4.3.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
    print(ul['class'])
    print(ul.attrs['class'])
    try:
        print(ul.attrs['name'])
    except:
        print("no attrs")
    print('----')
