from pyquery import PyQuery as pq

doc = pq(filename='../html5/4.3.4.1.html')
print(doc('#container .list li'))
# 依然是PyQuery类型
print(type(doc('#container .list li')))
