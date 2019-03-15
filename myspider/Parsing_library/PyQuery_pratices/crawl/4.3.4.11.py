from pyquery import PyQuery as pq

html = pq(filename='../html5/4.3.4.1.html')
# .逐层深入
a = html('.item-0.active a')
print(a)
print(a.text())

li = html('.item-0.active')
print(li)
# 返回li节点内部的所有的html文本
print(li.html())
print('------------')
# 我们选中多个节点，text()或者html()会返回什么内容？
li = html('li')
# 返回第一个li节点内的内部html文本
print(li.html())
print(li.text())
print(type(li.text()))
