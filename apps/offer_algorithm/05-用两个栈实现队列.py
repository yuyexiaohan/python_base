# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, node):
		# write code here
		self.stack1.append (node)

	def pop(self):
		# return xx
		if len (self.stack1) == 0 and len (self.stack2) == 0:
			return
		elif len (self.stack2) == 0:
			while len (self.stack1) > 0:
				self.stack2.append (self.stack1.pop ())

		return self.stack2.pop ()


ss = Solution()
ss.stack1 = [1,2,3,4]
ss.stack2 = [3,3,3,3]
aa = ss.pop()
bb = ss.push(9)
print(aa, bb, ss.stack1)
