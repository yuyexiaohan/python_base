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
		gap //= 2

if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	shell_sort(li)
	print(li)

"""
打印结果：复杂度：O(n)=n*n
[23, 45, 78, 88, 89, 90, 99, 129]

"""