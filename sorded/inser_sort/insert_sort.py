index = [1, 2, 0, 5, 9, 8, 10, 6, 4, 7]


def insert_sort(L):
    # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    for i in range(1, len(L)):
        # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
        # range(x-1,-1,-1):从x-1倒序循环到0
        print("第一层i:", i)
        for j in range(i - 1, -1, -1):
            # 判断：如果符合条件则交换
            print("第二层j:", j)
            if L[j] > L[j + 1]:
                temp = L[j + 1]
                L[j + 1] = L[j]
                L[j] = temp
            print(L)


if __name__ == '__main__':
    # main()
    insert_sort(index)
