import jieba
import wordcloud

txt = "啊打发打发发爱上对方就爱了就爱方法暗恋你解放啦地方啦"

w = wordcloud.WordCloud(width=1000, font_path="msyh.ttc", height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("py.png")
