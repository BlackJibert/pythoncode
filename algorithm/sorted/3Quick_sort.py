"""
快速排序思想:
　　快速排序将一个数组分成两个数组，再对两个数组独立排序，是个递归算法。
　　首先随机选出一个切分元素temp（一般为这个数组的第一个元素）,将小于temp的数放在temp的左边,将大于temp的数放在temp的右边。
　　快排和堆排序很像,他们都是将一个数组分成两个子数组,都属于递归算法。但是不同之处在于：快排空间复杂度为o（1）,而堆排为o（n）,
快排是原地排序，只需要一个很小的辅助栈，时间复杂度为NlogN
"""


def QuickSort(myList, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        # 递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


nums = [5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
print(nums)
print(QuickSort(nums, 0, len(nums) - 1))
