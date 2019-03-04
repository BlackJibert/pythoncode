from lxml import etree

html = etree.parse("../html5/4.1.4.3.html", etree.HTMLParser())
# html = etree.HTML(text)

result = html.xpath('//li[contains(@class,"li") and @name = "item2"]/a/text()')
print(result)
