# coding=utf-8 
# @Time : 2018/9/20 13:23 
# @Author : achjiang
# @File : code16_binary_search.py

# 二分查找
def binary_search(alist, item):
	"""递归版本的二分查找"""
	n = len(alist)
	if n > 0:
		mid = n//2
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			binary_search(alist[:mid],item)
		else:
			return binary_search(alist[mid+1:],item)
	return False

def binary_search_2(alist, item):
	"""非递归版本的查找"""
	n = len(alist)
	star = 0
	end = n - 1
	while star <= end:
		mid = (star + end)//2
		if alist[mid] == item:
			return True
		elif alist[mid] < item:
			star = mid + 1
		elif alist[mid] > item:
			end = mid-1
	return False



if __name__ == "__main__":
	li = [1, 3 ,6, 88, 89, 90, 99, 1100]
	result = binary_search(li,99)
	result1 = binary_search_2(li,99)
	print(result,result1)
