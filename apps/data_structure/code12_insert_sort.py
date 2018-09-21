# coding=utf-8 
# @Time : 2018/9/20 0:40 
# @Author : achjiang
# @File : code12_insert_sort.py

# 插入排序
def insert_sort(alist):
	"""插入排序"""
	n = len(alist)
	# 从右边的无序序列中取出多个元素进行
	# for j in range(1, n):
	# 	# i代表内存循环起始值
	# 	i = j
	# 	# 执行从右边的无序序列中取出的第一个元素，即i位置的元素，然后将其插入到前面的正确位置
	# 	while i > 0:
	# 		if alist[i] < alist[i-1]:
	# 			alist[i], alist[i-1] = alist[i-1], alist[i]
	# 			i -= 1
	# 		else:
	# 			break

	for i in range(1, n):
		# i代表内存循环起始值
		# i = j
		# 执行从右边的无序序列中取出的第一个元素，即i位置的元素，然后将其插入到前面的正确位置
		while i > 0:
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]
				i -= 1
			else:
				break

if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	insert_sort(li)
	print(li)

"""
打印结果：复杂度：O(n)=n*n
[23, 45, 78, 88, 89, 90, 99, 129]

"""