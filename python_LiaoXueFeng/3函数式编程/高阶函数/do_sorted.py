"""
假设我们用一组tuple表示学生名字和成绩：
L = [('Cob', 75), ('Ad', 67), ('Dart', 66), ('Lisa', 98)]

"""
# 1、请用sorted()对上述列表分别按名字排序：
L = [('Cob', 75), ('Ad', 67), ('Dart', 66), ('Lisa', 98)]


def by_name(t):
    return t[0]


L1 = sorted(L, key=by_name)
print(L1)


# 2、再按成绩从高到低排序：

def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
