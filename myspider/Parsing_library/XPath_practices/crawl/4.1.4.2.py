from lxml import etree

# 直接读取文本文件进行解析
html = etree.parse('../html5/4.1.4.1.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
