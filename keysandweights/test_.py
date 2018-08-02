from jieba.analyse import *
import requests

from pyecharts import WordCloud

with open('test.txt', encoding='utf-8') as f:
    data = f.read()
keys_ = []
values_ = []
for keyword, weight in extract_tags(data, topK=50, withWeight=True):
    keys_.append(keyword)
    values_.append(weight)

print(keys_)
print(values_)
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", keys_, values_, word_size_range=[20, 100])
wordcloud.render()