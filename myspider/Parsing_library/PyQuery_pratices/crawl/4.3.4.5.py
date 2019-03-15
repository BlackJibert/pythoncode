from pyquery import PyQuery as pq

doc = pq(filename='../html5/4.3.4.1.html')
items = doc('.list')
print(type(items))
print(items)
# find方法会找出所有符合条件的子孙节点
lis = items.find('li')
print(type(lis))
print(lis)
# childrn()方法是子节点
lis = items.children('.active')
print(type(lis))
print(lis)
