from bs4 import BeautifulSoup

html = open('../html5/4.2.4.1.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:', soup.a.next_sibling)
print('Previous Sibling: ', soup.a.previous_sibling)
print('Next Siblings:', list(enumerate(soup.a.next_siblings)))
print('Previous Siblings: ', list(enumerate(soup.a.previous_siblings)))
