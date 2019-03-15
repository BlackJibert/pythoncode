from pyquery import PyQuery as pq

doc = pq(filename='../html5/4.3.4.1.html')
# 要注意：选择class为li的节点内部class为item-0和active的节点,item-1和active之间没有空格
li = doc('.list .item-1.active')
print(li)
# 选择兄弟节点
print(li.siblings())
# 筛选兄弟节点
print(li.siblings('.item-0'))
