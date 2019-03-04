from lxml import etree

html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())

# 1、我们获取第一个li节点，中括号中传入数字1,而不是0
response1 = html.xpath('//li[1]/a/text()')
print(response1)

# 2、选取了最后一个li节点，中括号中传入last()即可
response2 = html.xpath('//li[last()]/a/text()')
print(response2)

# 3、选取了位置小于3的li节点，也就是位置序号为1和2的节点
response3 = html.xpath('//li[position()<3]/a/text()')
print(response3)

# 4、选取了倒数第三个li节点，中括号中传入了last()-2即可
response4 = html.xpath('//li[last()-2]/a/text()')
print(response4)
