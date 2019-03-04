from lxml import etree

html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())
# *代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取，返回的是element类型
result = html.xpath('//*')
print(result)

# 获取所有的li节点
result2 = html.xpath('//li')
print(result2[0])

# 获取第一个li节点
result2 = html.xpath('//div')
print(result2)
