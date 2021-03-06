# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
	def minNumberInRotateArray(self, rotateArray):
		# write code here
		if len (rotateArray) == 0:
			return 0
		front = 0
		rear = len (rotateArray) - 1
		minVal = rotateArray[0]

		if rotateArray[front] < rotateArray[rear]:
			return rotateArray[front]
		else:
			while (rear - front) > 1:
				mid = (front + rear) // 2
				if rotateArray[mid] >= rotateArray[front]:
					front = mid
				elif rotateArray[mid] <= rotateArray[rear]:
					rear = mid
				elif rotateArray[front] == rotateArray[rear] == rotateArray[mid]:
					for i in range (1, len (rotateArray)):
						if rotateArray[i] < minVal:
							minVal = rotateArray[i]
							rear = i
			minVal = rotateArray[rear]
			return minVal

s_examp = Solution()
rotateArray = [5,6,7,2,2,3]
array_new = s_examp.minNumberInRotateArray(rotateArray)
print(array_new)
