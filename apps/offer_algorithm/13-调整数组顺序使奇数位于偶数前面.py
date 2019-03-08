# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
	def reOrderArray(self, array):
		# write code here
		qi, ou = [], []
		for i in array:
			qi.append(i) if i%2 == 1 else ou.append(i)
		return qi + ou

	def re_order_array(self, array):
		# 使用lambda式
		return sorted(array, key=lambda c:c%2, reverse=True)

	def print_function(self, example):
		# 打印函数
		print(example)


if __name__ == '__main__':
	example1 = Solution()
	array = [2,3,4,5,6,8,9,7,11,9]
	array_order = example1.reOrderArray(array)
	array_order1 = example1.re_order_array(array)
	example1.print_function(array_order)
	example1.print_function(array_order1)