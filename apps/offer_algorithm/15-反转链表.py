# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
输入一个链表，反转链表后，输出新链表的表头。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
	# 返回ListNode
	def ReverseList(self, pHead):
		# write code here
		pReversedHead = None
		pNode = pHead
		pPrev = None
		while pNode != None:
			pNext = pNode.next
			if pNext == None:
				pReversedHead = pNode

			pNode.next = pPrev
			pPrev = pNode
			pNode = pNext
		return pReversedHead