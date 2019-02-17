# GovRptWordCloudV1.py
from random import randint

import jieba
import wordcloud
from scipy.misc import imread


# 设置颜色函数color_func
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = randint(120, 250)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(randint(60, 120)) / 255.0)
    # h = s = l
    # print("hsl({}, {}%, {}%)".format(h, s, l))
    # return "hsl({}, {}%, {}%)".format(h, s, l)
    # 黑色
    return "black"


mask = imread("fivestars.jpg")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = "".join(ls)
# 生成wordcloud的对象

w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white"
                        , max_words=15, mask=mask, color_func=random_color_func)
w.generate(txt)
w.to_file("grwordcloud11.png")
