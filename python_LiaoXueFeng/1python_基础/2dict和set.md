# dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85

## 1、判断key是否存在

   - 'Thomas' in d
   - d.get('Thomas')
## 2、要删除一个key，用pop(key)方法，对应的value也会从dict中删除
- d.pop('Bob')

## 3、和list比较，dict有以下几个特点：

- 查找和插入的速度极快，不会随着key的增加而变慢；
- 需要占用大量的内存，内存浪费多。

##4、而list相反：

- 查找和插入的时间随着元素的增加而增加；
- 占用空间小，浪费内存很少。

##5、dict的key必须是不可变对象

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key




# set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

## 1、要创建一个set，需要提供一个list作为输入集合
例如：
    s = set([1, 2, 3, 1 ])
输出为：
    {1, 2, 3}

## 2、重复元素在set中自动被过滤：


## 3、通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
## 4、通过remove(key)方法可以删除元素：

