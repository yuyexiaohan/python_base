# coding=utf-8 
# @Time : 2018/9/20 1:11 
# @Author : achjiang
# @File : code13_shell_sort.py

# 希尔排序
def shell_sort(alist):
	"""希尔排序"""
	n = len(alist)
	gap = n // 2 # 步长,除法取整
	print('gap:',gap)
	# i = gap
	# for i in range(gap, n):
	# 	i = [gap, gap+1, gap+2, gap+3... n-1]
	#       while:
	#           if alist[i] < alist[i-gap]:
	#               alist[i], alist[i-gap] = alist[i-gap], alist[i]
	# gap变化到零之前，插入算法执行次数
	while gap > 0:
	# 同一列找最小值
		for j in range(gap, n):
			i = j
		# 内部循环
			while i > 0 :
				if alist[i] < alist[i-gap]:
					alist[i], alist[i-gap] = alist[i-gap], alist[i]
					i -= gap
				else:
					break
				# 直接退出循环是因为希尔排序中前面内容的
				# 排序，都是由小到大，当目前这个与最大值
				# 比较也是最大时，就默认这个步长的数据就是
				# 由小到大排序。这样跳出，会节省步骤。当然
				# 也是可以不退出，直到i<=0条件后退出。
		gap //= 2

if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	shell_sort(li)
	print(li)

"""
打印结果：复杂度：O(n)=n*n
[23, 45, 78, 88, 89, 90, 99, 129]

"""