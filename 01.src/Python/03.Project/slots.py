#!/usr/bin/env python


from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')  # 仅对当前类实例起作用，限制类能添加的属性和方法


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


s = Student()
s.set_name = "micale"  # 绑定一个方法
print(s.set_name)
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(24)
print(s.age)
Student.set_score = set_score  # 给类绑定一个方法
s.set_score(34)
print(s.score)