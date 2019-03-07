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
		return base**exponent

	def printFount(self, base):
		print(base)

example = Solution()
base_int_mi = example.Power(0.1, 2)
base_int_mi1 = example.Power1(0, 2)
example.printFount(base_int_mi)
example.printFount(base_int_mi1)

