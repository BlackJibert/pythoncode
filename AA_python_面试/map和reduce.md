# 1、利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
    def normalize(name):
        str1 = ''
        for key, value in enumerate(name):
            if key == 0:
                str1 += value.upper()
            else:
                str1 += value.lower()
        return str1
    
    L1 = ['adam', 'LISA', 'barT']
    print(L1)
    L2 = list(map(normalize, L1))
    print(L2)

# 2、Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

    from functools import reduce
    def prod(L):
        return reduce(cheng_,L)
    def cheng_(x,y):
        return x*y
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')
    
    
# 3、利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# str2int函数

    from functools import reduce
    
    CHAR_TO_INT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    
    def str2int(s):
        ints = map(lambda ch: CHAR_TO_INT[ch], s)
        return reduce(lambda x, y: x * 10 + y, ints)
    
    print(str2int('0'))
    print(str2int('12300'))
    print(str2int('0012345'))
    
    CHAR_TO_FLOAT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '.': -1
    }
    
    def str2float(s):
        nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
        point = 0
        def to_float(f, n):
            nonlocal point
            if n == -1:
                point = 1
                return f
            if point == 0:
                return f * 10 + n
            else:
                point = point * 10
                return f + n / point
        return reduce(to_float, nums, 0.0)
    
    print(str2float('0'))
    print(str2float('123.456'))
    print(str2float('123.45600'))
    print(str2float('0.1234'))
    print(str2float('.1234'))
    print(str2float('120.0034'))
