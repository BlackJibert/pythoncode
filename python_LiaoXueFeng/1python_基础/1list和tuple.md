# list
Python内置的一种数据类型是列表：list

list是一种有序的集合，可以随时添加和删除其中的元素。
例如：
    classmates = ['Michael', 'Bob', 'Tracy']

## 1、len()函数可以获得list元素的个数
## 2、索引从0开始

- 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
- 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素

## 3、末尾追加 append('xx')

-list是一个可变的有序表，所以，可以往list中追加元素到末尾

## 4、也可以把元素插入到指定的位置，比如索引号为1的位置
-classmates.insert(1, 'Jack')

## 5、末尾删除pop()
-classmates.pop()

## 6、要删除指定位置的元素，用pop(i)方法，其中i是索引位置
 - classmates.pop(1)
 
## 7、list里面的元素的数据类型也可以不同

# tuple
另一种有序列表叫元组：tuple
tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
例如：
    classmates = ('Michael', 'Bob', 'Tracy')
现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

#定义： t = (1,)
可以使用
sum() 或者len()
对tuple中进行求和或者求长度



