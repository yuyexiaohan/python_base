# coding=utf-8 
# @Time : 2018/9/20 10:39 
# @Author : achjiang
# @File : code14_quick_sort.py

# 快速排序
def quick_sort(alist, star, end):
	"""快速排序"""
	if star >= end:
		return
	mid_value = alist[star]
	low = star
	high = end
	while low < high:
		# 注意；必须先左移再右移，因为我们是先拿最左边的元素进行比较的
		# 左移i
		while low < high and alist[high] >= mid_value:
			high -= 1
		alist[low] = alist[high]
		# 右移
		while low < high and alist[low] < mid_value:
			low += 1
		alist[high] = alist[low]
	# 	从循环中退出时，low==high
	alist[low] = mid_value

	# 使用递归调用，实现分开高位和低位的排序
	# low左边部分排序
	quick_sort(alist, star, low-1)
	# low右边的部分排序
	quick_sort(alist, low+1, end)


if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	quick_sort(li,0,len(li)-1)
	print(li)

"""
打印结果：复杂度：O(n)=n*n
[23, 45, 78, 88, 89, 90, 99, 129]

"""
