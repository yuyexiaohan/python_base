# coding=utf-8
# Time : 2019/2/14
# Author : achjiang
"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


class Solution:
    def power(self, base, exponent):
        # 方法1：直接判断法
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

    def power1(self, base, exponent):
        # 方法2：直接使用python的方法
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

    def power2(self, base, exponent):
        # 方法3：位移判断法
        try:
            ret = self.power_value(base, abs(exponent))
            if exponent < 0:
                return 1.0 / ret
        except ZeroDivisionError:
            print("Error: base is zero")
        else:
            return ret

    def print_fount(self, base):
        # 打印函数
        print(base)


example = Solution()
base_int_mi = example.power(0.1, 2)
base_int_mi1 = example.power1(0, 2)
base_int_mi2 = example.power2(0, 2)
example.print_fount(base_int_mi)
example.print_fount(base_int_mi1)
example.print_fount(base_int_mi2)
