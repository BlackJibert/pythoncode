from pyquery import PyQuery as pq

html = pq(filename='../html5/4.3.4.1.html')
li = html('.item-0.active')
print(li)
print(str(li))
