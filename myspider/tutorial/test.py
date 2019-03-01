class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls, te):
        print('func2')
        print(cls.bar)
        print(te)
        cls().func1()  # 调用 foo 方法


# A.func2()  # 不需要实例化

# t = A()
# t.func1()
A.func2("hh")
