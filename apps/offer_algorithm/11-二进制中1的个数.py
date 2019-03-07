# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

#
# class Solution:
# 	def NumberOf1(self, n):
# 		# write code here
class Solution:
	def NumberOf1(self, n):
		# write code here
		return bin (n).replace ("0b", "").count ("1") if n >= 0 else bin (2 ** 32 + n).replace ("0b",
				                                                                                        "").count ("1")


class Solution1:
	def NumberOf1(self, n):
		# write code here
		count = 0
		if n < 0:
			n = n & 0xffffffff
		while n != 0:
			count += 1
			n = (n - 1) & n
		return count

example_new = Solution()
example_new1 = Solution1()
n_bin = example_new.NumberOf1(7)
n_bin1 = example_new.NumberOf1(-1)
n_bin2 = example_new1.NumberOf1(7)
n_bin3 = example_new1.NumberOf1(-1)
print("n_bin:", n_bin, "n_bin1", n_bin1, "n_bin2:", n_bin2, "n_bin3", n_bin3)