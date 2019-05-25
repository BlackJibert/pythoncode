def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    # 初始序列
    it = _odd_iter()
    while True:
        # 返回序列的第一个数
        n = next(it)
        yield n
        # 构造新序列
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
