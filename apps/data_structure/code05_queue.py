# coding=utf-8 
# @Time : 2018/9/19 23:01 
# @Author : achjiang
# @File : code05_queue.py

class Queue(object):
	"""队列"""
	def __init__(self):
		"""构造函数，实现一个存储"""
		self.__list = []

	def enqueue(self, item):
		"""往队列里添加一个item元素"""
		self.__list.append(item)
		# self.__list.insert(0, item)

	def dequeue(self):
		"""从队列头部删除一个元素"""
		return self.__list.pop()
		# return self.__list.pop(0)

	def is_empty(self):
		"""判断队列是否为空"""
		return self.__list is None

	def size(self):
		"""返回队列长度"""
		return len(self.__list)

if __name__ == "__main__":
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())

"""
打印结果：
3
2
1
"""