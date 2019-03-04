from lxml import etree

html = etree.parse('../html5/4.1.4.4.html', etree.HTMLParser())
# html = etree.HTML(text)

# 1、调用ancestor轴，获取所有祖先节点，后跟两个冒号，然后是节点选择器，*星号匹配所有节点
result1 = html.xpath('//li[1]/ancestor::*')
print(result1)

# 2、冒号后面加个div，这样得到结果只有div这个祖先节点
result2 = html.xpath('//li[1]/ancestor::div[@class="div_2"]/text()')
print(result2)

# 3、调用了attribute轴，可以获取所有属性值，后面跟着是*，这代表获取节点的所有属性，返回就是li节点的所有属性值
result3 = html.xpath('//li[1]/attribute::*')
print(result3)

# 4、调用了child轴，可以获取所有直接子节点，选取href属性为link1.html的a节点，我另外又加了限定条件
result4 = html.xpath('//li[1]/child::*[@href="link1.html"]//text()')
print(result4)

# 5、调用了descendant轴，可以获取所有子孙节点，我们又加了限定条件获取span节点
result5 = html.xpath('//li[1]/descendant::span')
print(result5)

# 6、调用了following轴，可以获取当前节点之后的所有节点，使用的是*匹配，后面又加了索引选择
# 这里所谓“之后”是指不包括它的子节点，位于它后面的所有节点，包含不同级的
result6 = html.xpath('//li[1]/following::*')
print(result6)

# 7、调用了following-sibling轴，可以获取当前节点之后的所有同级节点
result7 = html.xpath('//li[1]/following-sibling::*[@class="item-4"]/a/text()')
print(result7)
