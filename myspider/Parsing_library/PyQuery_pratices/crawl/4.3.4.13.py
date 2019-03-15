from pyquery import PyQuery as pq

html = pq(filename='../html5/4.3.4.1.html')
li = html('.item-0.active')
print(li)
# 增加name属性，值为link
li.attr('name', 'link')
print(li)

li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)
