from lxml import etree

html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())

# /或//用于查找元素的子节点或子孙节点

# 用于获取所有li节点的所有直接a节点
response = html.xpath('//li/a')
print(response)

# 获取ul节点下的所有子孙a节点
response2 = html.xpath('//ul//a')
print(response2)

# 没有任何输出，因为ul下没有直接的a子节点
response3 = html.xpath('//ul/a')
print(response3)
