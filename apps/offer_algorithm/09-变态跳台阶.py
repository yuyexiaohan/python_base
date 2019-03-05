# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
思路：跳法种类是前所有种类和+1即等比数列，即1-2^0,2-2^1,3-2^2即，number = 2^(number-1)
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        star = 1
        if number >= 2:
            for i in range(number-1):
                star = star * 2
        return star