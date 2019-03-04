from lxml import etree

html = etree.parse("../html5/4.1.4.1.html", etree.HTMLParser())
# 选取class为item-1的li节点
response = html.xpath('//li[@class = "item-1"]')
print(response)
