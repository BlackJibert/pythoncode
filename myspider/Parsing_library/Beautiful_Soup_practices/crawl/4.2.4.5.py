from bs4 import BeautifulSoup

html = open('../html5/4.2.4.1.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')
# 得到的结果是直接子节点的列表
print(soup.p.contents)

# 调用childer属性得到相应得结果，为生成器类型
print(soup.p.children)
for i, child2 in enumerate(soup.p.children):
    print(i, child2)

# 得到所有子孙节点的话，调用descendants属性,结果为生成器，descendants会递归查询所有子节点
print(soup.p.descendants)
for i, child2 in enumerate(soup.p.descendants):
    print(i, child2)
