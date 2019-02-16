# CalStatisticsV1

def getNum():
    nums = []
    isNumStr = input("请输入数字(回车退出)：")
    while isNumStr != "":
        nums.append(eval(isNumStr))
        isNumStr = input("请输入数字(回车退出)：")
    return nums


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)


def dev(numbers, mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


if __name__ == '__main__':
    n = getNum()
    m = mean(n)
    print("平均值:{},方差:{:.2},中位数:{}".format(m, dev(n, m), median(n)))
