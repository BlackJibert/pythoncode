from lxml import etree

html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())
# 获取所有的a节点，然后获取其父节点，再获取class属性
result = html.xpath('//a[@href = "link4.html"]/../@class')
print(result)
# parent:: 来获取父节点,注意有个*
result2 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result2)
