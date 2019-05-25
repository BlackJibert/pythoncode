# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    s = str(n)
    for i in range((len(s) + 1) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
