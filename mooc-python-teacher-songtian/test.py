tf = open("./py/7-the-seventh-week/test.txt", "a+", encoding="utf-8")
for line in tf:
    print(line)
s = ["嘿嘿1", "哇哇1", "游戏1"]
tf.writelines(s)
# tf.seek(1)
for line in tf:
    print(line)

tf.close()
