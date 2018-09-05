# coding=utf-8 
# @Time : 2018/9/5 23:20 
# @Author : achjiang
# @File : algorithm_03快排.py

# 使用快排进行数据的排序
# 分析：这里主要用到的是，递归调用
# 将默认选择的参照数，与剩余部分作比较，大于的部分分为一个列表
# 小于的部分分为一个列表，然后递归调用函数，依次分组


def quicksort(li):
	'''快速排序'''
	if len(li) < 2:
		return li
	else:
		li_min,li_max = [],[]
		base = li[0]
		for i in li[1:]:
			if i <= base:
				li_min.append(i)
			else:
				li_max.append(i)
		return quicksort(li_min) + [base] + quicksort(li_max)

list_01 = [3,6,8,4,9,12,2,44,67,22,13]
# 打印结果：[2, 3, 4, 6, 8, 9, 12, 13, 22, 44, 67]
a = quicksort(list_01)
print(a)

