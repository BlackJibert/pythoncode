import jieba

words = jieba.lcut("哈阿哦怕迪地方斯发地方哈阿斯蒂芬哈哈还会哈阿三发射点发啊手动阀打发和防守对方红辣椒鲁大师考分亲和力看看就拉风的")
for word in words:
    if len(word) == 1:
        continue
    else:
        print(word)
# print(words)
