# CalThreeKingdomsV2.py

import jieba

txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
# 需要不断运行优化排除词库
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "主公", "军士",
            "军马", "左右", "引兵", "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵", "陛下",
            "次日", "一人", "都督", "人马", "不知", "汉中", "只见", "众将", "后主", "蜀兵", "上马", "大叫", "太守", "此人",
            "夫人", "先生"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

# <三国演义>人物出场顺序top10
# 曹操         1451
# 孔明         1383
# 刘备         1252
# 关羽          784
# 张飞          358
# 吕布          300
# 赵云          278
# 孙权          264
# 司马懿         221
# 周瑜          217
