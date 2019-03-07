from bs4 import BeautifulSoup

# html = open('../html5/4.2.4.2.html', 'r', encoding='utf-8')
html = """
<html>
<body>
<p class = "story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elise" class="sister" id="link1">Bob
    </a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie
    </a>
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print("Parents:")
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
# print(list(soup.a.parents)[0].attrs['id'])
