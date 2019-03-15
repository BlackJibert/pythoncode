from pyquery import PyQuery as pq

html = pq(filename='../html5/4.3.4.1.html')
# 调用items()方法后，会得到一个生成器
lis = html('li').items()
for li in lis:
    print(li, type(li))
