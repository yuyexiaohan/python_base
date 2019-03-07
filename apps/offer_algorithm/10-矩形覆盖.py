# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


class Solution:
	def rectCover(self, number):
	# write code here
		if number == 0:
			return 0
		list_new = [1,2]
		if number >= 3:
			for i in range(3, number+1):
				list_new[(i+1)%2] = list_new[0] + list_new[1]
		return list_new[(number+1)%2]


class SolutionNew:
	def rectCover(self, number):
	# write code here
		if number == 0:
			return 0
		if number == 1:
			return 1
		if number == 2:
			return 2
		if number >= 3:
			return self.rectCover(number-1) + self.rectCover(number-2)

sample_1 = Solution()
sample_new = SolutionNew()
n = sample_1.rectCover(5)
n_new = sample_1.rectCover(7)
print("n:", n, '/n', "n_new:", n_new)
