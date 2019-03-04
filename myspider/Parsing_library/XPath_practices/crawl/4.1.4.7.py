from lxml import etree

html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())
#  / 选取直接子节点
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 获取li的class为item-0的所有文本
result2 = html.xpath('//li[@class="item-0"]//text()')
print(result2)
