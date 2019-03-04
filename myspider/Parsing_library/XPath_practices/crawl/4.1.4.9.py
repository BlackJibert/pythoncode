from lxml import etree

html = etree.parse('../html5/4.1.4.2.html', etree.HTMLParser())

# 通过contains()方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所传入的属性值，就可以完成匹配
response = html.xpath('//li[contains(@class,"li-second")]/a/text()')
print(response)
