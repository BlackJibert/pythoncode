from pyquery import PyQuery as pq

doc = pq(filename='../html5/4.3.4.1.html')
print(doc('li'))
