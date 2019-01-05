# "二分查找非递归"
def binary_search(x):
    a = [1, 2, 3, 4, 5, 6, 7]
    n = len(a)
    low = 0
    high = n - 1
    time = 0
    while (low < high):
        mid = (low + high) // 2
        if x < a[mid]:
            high = mid - 1
            time = time + 1
        elif x > a[mid]:
            low = mid + 1
            time = time + 1
        else:
            print("已经找到%d,经过%d次查找" % (x, time))
            return True
    print('没有找到')
    return False


# binary_search(2)

# "递归二分查找"
def recursion_binary_serch(a, x):
    # a = [1,2,3,4,5,6,7]
    n = len(a)
    time = 0
    mid = n // 2
    if x < a[mid]:
        time = time + 1
        recursion_binary_serch(a[0:mid], x)
    elif x > a[mid]:
        time = time + 1
        recursion_binary_serch(a[mid:], x)
    else:
        print("已经找到%d,经过%d次查找" % (x, time + 1))
        return True
    # print('没有找到')
    return False


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    if recursion_binary_serch(a, 3):
        print("已经找到")
