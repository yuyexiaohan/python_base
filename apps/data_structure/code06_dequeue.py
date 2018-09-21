# coding=utf-8 
# @Time : 2018/9/19 23:11 
# @Author : achjiang
# @File : code06_dequeue.py

class Dequeue(object):
	"""双端队列"""

	def __init__(self):
		"""构造函数，实现一个存储"""
		self.__list = []

	def add_front(self, item):
		"""往队列头添加一个item元素"""
		self.__list.insert(0, item)

	def add_rear(self, item):
		"""往队列尾添加一个item元素"""
		self.__list.append(item)

	def remove_front(self):
		"""从队列头部删除一个元素"""
		return self.__list.pop(0)

	def remove_rear(self):
		"""从队列尾部删除一个元素"""
		return self.__list.pop()

	def is_empty(self):
		"""判断双端队列是否为空"""
		return self.__list is None

	def size(self):
		"""返回队列长度"""
		return len(self.__list)

if __name__ == "__main__":
	deq = Dequeue()
	deq.add_front(1)
	deq.add_front(2)
	deq.add_front(3)
	print(deq.remove_front())
	print(deq.remove_front())
	print(deq.remove_front())

	deq.add_rear(11)
	deq.add_rear(12)
	deq.add_rear(13)
	print(deq.remove_rear())
	print(deq.remove_rear())
	print(deq.remove_rear())

"""
打印结果：
3
2
1
13
12
11
"""

