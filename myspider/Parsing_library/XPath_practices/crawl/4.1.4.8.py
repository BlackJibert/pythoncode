from lxml import etree

html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())
# 加上@href即可获取节点的href属性值
result = html.xpath('//li/a/@href')
print(result)
