# coding=utf-8 
# @Time : 2018/8/24 23:22 
# @Author : achjiang
# @File : new_init.py

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
print(v1.__str__())
v2 = Vector(5, -2)
print(v2)
print(v1 + v2)


