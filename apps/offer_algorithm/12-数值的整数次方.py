# coding=utf-8
# Time : 2019/2/14
# Author : achjiang
"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        while exponent > 1:
            base *= base
            exponent -= 1
        return base

    def Power1(self, base, exponent):
        # 方法1：直接使用python的方法
        return base**exponent

    def power_value(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        ret = self.power_value(base, exponent >> 1)
        ret *= ret
        if exponent & 1 == 1:
            ret *= base
        return ret

    def Power2(self, base, exponent):
        try:
            ret = self.power_value(base, abs(exponent))
            if exponent < 0:
                return 1.0 / ret
        except ZeroDivisionError:
            print("Error: base is zero")
        else:
            return ret

    def printFount(self, base):
        print(base)


example = Solution()
base_int_mi = example.Power(0.1, 2)
base_int_mi1 = example.Power1(0, 2)
example.printFount(base_int_mi)
example.printFount(base_int_mi1)
