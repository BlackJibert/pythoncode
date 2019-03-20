def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()
# next() 返回迭代器的下一个项目
print(next(g))
print("*" * 20)
print(next(g))
