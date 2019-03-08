# coding=utf-8
# Time : 2019/2/14
# Author : achjiang

"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if k > len(res) or k < 1:
            return
        return res[-k]


class SolutionNew:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None

        pAhead = head
        pBhead = None

        for i in range(k - 1):
            if pAhead.next is not None:
                pAhead = pAhead.next
            else:
                return None

        pBhead = head
        while pAhead.next is not None:
            pAhead = pAhead.next
            pBhead = pBhead.next
        return pBhead


example = Solution()
the_k = example.FindKthToTail(1, 1)
print(the_k)
