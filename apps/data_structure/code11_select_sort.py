# coding=utf-8 
# @Time : 2018/9/20 0:15 
# @Author : achjiang
# @File : code11_select_sort.py

# 选择排序
def select_sort(alist):
	"""选择排序"""
	n = len(alist)
	for j in range(n-1):
		min_index = j
		for i in range(j+1, n):
			if alist[min_index] > alist[i]:
				min_index = i
		alist[j], alist[min_index] = alist[min_index], alist[j]

if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	select_sort(li)
	print(li)

"""
打印结果：复杂度：O(n)= n*n 
[23, 45, 78, 88, 89, 90, 99, 129]

"""