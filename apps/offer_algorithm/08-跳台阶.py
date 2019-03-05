# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang

"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
"""


class Solution:
	def JumpFloor(self, number):
		# write code here
		res = [1, 2]
		if number <= 0 or not isinstance(number, int):
			return 0
		elif number == 1:
			return 1
		elif number == 2:
			return 2
		else :
			for i in range(3, number+1):
				res[(i + 1) % 2] = res[0] + res[1]
			return res[(number + 1) % 2]




ss = Solution()
a = ss.JumpFloor(5)
print(a)