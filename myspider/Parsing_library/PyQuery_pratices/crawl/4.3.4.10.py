from pyquery import PyQuery as pq

html = pq(filename='../html5/4.3.4.1.html')
a = html('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

# 匹配到多个属性时，需要使用遍历，否则只有匹配到第一个节点的属性
a = html('a')
print(a, type(a))
print(a.attr.href)

# 遍历
a = html('a')
for item in a.items():
    print(item.attr.href)
