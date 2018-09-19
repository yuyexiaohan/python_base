# coding=utf-8 
# @Time : 2018/9/19 22:39 
# @Author : achjiang
# @File : code04_stack.py


class Stack(object):
	"""栈"""
	def __init__(self):
		self.__list = [] # 创建私有元素

	def push(self, item):
		"""添加一个新的item元素到栈顶"""
		self.__list.append(item)

	def pop(self):
		"""弹出栈顶的元素"""
		return self.__list.pop()


	def peek(self):
		"""返回栈顶的元素"""
		if self.__list:
			return self.__list[-1]
		else:
			return None

	def is_empty(self):
		"""判断栈是否为空"""
		return self.__list is None

	def size(self):
		"""返回栈的元素个数"""
		return len(self.__list)

if __name__ == "__main__":
	s = Stack()
	print(s.is_empty())
	s.push(1)
	s.push(2)
	s.push(3)
	print (s.pop())
	print (s.pop())
	print (s.pop())
	s.push(99)
	print (s.peek())
	print (s.size())
	print (s.is_empty())
