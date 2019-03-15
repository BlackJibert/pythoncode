from pyquery import PyQuery as pq

doc = pq(filename='../html5/4.3.4.1.html')
items = doc('.list')
# 获取直接父节点
container = items.parent()
print(type(container))
print(container)
# 返回所有的祖先节点
parents = items.parents('#wrap')
print(type(parents))
print(parents)
