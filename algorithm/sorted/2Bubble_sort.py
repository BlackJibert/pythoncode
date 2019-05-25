"""
冒泡排序的思想:
每次比较两个相邻的元素,如果他们的顺序错误就把他们交换过来
"""


def bubble_sort(num):
    for i in range(len(num) - 1):

        for j in range(len(num) - 1 - i):
            # 升序排列,将">"改为"<"为降序排列
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


nums = [5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
after_sorted = bubble_sort(nums)
print(after_sorted)
