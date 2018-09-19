# coding=utf-8 
# @Time : 2018/9/19 23:43 
# @Author : achjiang
# @File : code10_ bubble_sort.py

def bubble_sort(alist):
	"""#1 第1版：冒泡排序"""
	n = len(alist)
	for j in range(n-1):
		for i in range(n-(j+1)):
			# 这层循环是一次从头到尾
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]

def bubble_sort_02(alist):
	"""#1 第2版：冒泡排序"""
	n = len(alist)
	for j in range(n-1):
		count = 0
		for i in range(n-(j+1)):
			# 这层循环是一次从头到尾
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				count += 1
		if 0 == count:
			# 说明第一次遍历数据就是有限的
			return

if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	bubble_sort(li)
	print(li)

"""
打印结果：
[23, 45, 78, 88, 89, 90, 99, 129]

"""