from jieba.analyse import *

with open('test.txt') as f:
    data = f.read()
for keyword, weight in extract_tags(data, withWeight=True):
    print('%s %s' % (keyword, weight))
