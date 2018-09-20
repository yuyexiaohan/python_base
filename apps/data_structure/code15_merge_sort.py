# coding=utf-8 
# @Time : 2018/9/20 11:57 
# @Author : achjiang
# @File : code15_merge_sort.py

# 归并排序

def merge_sort(alist):
	"""归并排序"""
	n = len(alist)
	if n <= 1:
		return alist
	mid = n//2
	# 采用分离，分为左边部分,嵌套调用直到n=1
	left_li = merge_sort(alist[:mid])
	# 采用分离，分为右边部分,嵌套调用直到n=1
	right_li = merge_sort(alist[mid:])

	#2 将两个有序子集合并到一个集合中去
	left_pointer, right_pointer = 0, 0
	result = []
	while left_pointer < len(left_li) and right_pointer < len(right_li):
		# 判断左边或右边是否越界
		if left_li[left_pointer] < right_li[right_pointer]:
			result.append(left_li[left_pointer])
			left_pointer += 1
		else:
			result.append(right_li[right_pointer])
			right_pointer += 1
		# 不管是left_li或right_li走到头，后面没有的部分就直接将另一个剩余部分加入到result中去
	result += left_li[left_pointer:]
	result += right_li[right_pointer:]
	return result

if __name__ == "__main__":
	li = [99, 78 ,129, 88, 90, 23, 45, 89]
	sorted_li = merge_sort(li)
	print(li)
	print(sorted_li)

"""
打印结果：复杂度：O(n)=nlogn
[23, 45, 78, 88, 89, 90, 99, 129]

"""