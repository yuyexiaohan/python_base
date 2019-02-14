# coding=utf-8
# Time : 2019/2/14
# Author : achjiang
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
# -*- coding:utf-8 -*-


class Solution():
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == []:
            return False
        row_count = len(array)
        col_count = len(array[0])
        i = row_count - 1
        j = 0

        while i >= 0 and j < col_count:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False


li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
s = Solution()
rel1 = s.Find(16, li)
rel2 = s.Find(17, li)
print(rel1, rel2)
