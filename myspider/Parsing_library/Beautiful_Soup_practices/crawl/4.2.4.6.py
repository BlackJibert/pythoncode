from bs4 import BeautifulSoup

html = open('../html5/4.2.4.1.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
# 找到所有的a，它的父亲p节点，输出结果是p节点及其内部的内容
# print(soup.a.parent)

# 生成器类型，获取所有的祖先节点
print(type(soup.a.parents))
# 用列表输出了它的索引和内容
print(list(enumerate(soup.a.parents)))
