# coding=utf-8 
# @Time : 2018/9/3 23:22 
# @Author : achjiang
# @File : algorithm_二分法排序.py
import os

# 一行代码计算0~100的和
# a = sum(range(0,101))
# print(a)

# 二分法查找
def find_tow(li,x):
	star_index,end_index = 0,len(li)-1
	li_new = sorted(li)
	i = 0
	print('li_new：',li_new)
	while star_index <= end_index:
		mid = int((star_index + end_index)/2)
		# print(mid,li_new[mid])
		if li_new[mid] < x:
			star_index = mid + 1
		elif li_new[mid] > x:
			end_index = mid - 1
		else:
			print('查找结果为：元素%s的索引序号是'%x,mid,'\n总共查找次数为%s次:'%i)
			return {mid:li_new[mid]}
		i += 1
	return print('查找结果为：列表中未找到该元素','\n总共查找次数为%s次:'%i)

li = [1,2,3,6,8,9,10,23,45,5]
a = find_tow(li,5)

