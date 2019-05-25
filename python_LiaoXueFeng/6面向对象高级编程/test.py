from types import MethodType


class Student(object):
    pass


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法

s2 = Student()
s2.set_age(25)
