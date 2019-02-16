# CalHamletV1.py 统计单词出现频次

# 获得干净的，归一化的文本
def getText():
    txt = open('hamlet.txt', 'r').read()
    txt = txt.lower()
    # 去掉特殊符号
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~‘’':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
# 用空格分隔，组成列表
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
