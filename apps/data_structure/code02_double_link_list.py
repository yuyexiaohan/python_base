# coding=utf-8 
# @Time : 2018/9/19 15:00 
# @Author : achjiang
# @File : code02_double_link_list.py
# from . import code01_01single_link_list # 单链表和双链表有很多相同的样子，所以这里就按照

class Node(object):
	"""节点"""
	def __init__(self, item):
		self.elem = item
		self.next = None
		self.prev = None

class Dpuble_link_list(object):
	"""双向列表"""

	def __init__(self, node=None):
		"""初始化，链表初始指向位置为空"""
		self.__head = node  # 私有变量是双下滑线

	def is_empty(self):
		"""链表是否为空"""
		# pep8推荐比较使用is
		return self.__head is None

	def length(self):
		"""链表长度"""
		# cur游标，用来移动遍历节点
		cur = self.__head
		# count记录数量
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur != None:
			print (cur.elem, end=" ")  # 打印cur.elem??
			cur = cur.next

	def add(self, item):
		"""链表头部添加元素"""
		node = Node (item)  # 实例化为一个节点数据
		node.next = self.__head  # 将新节点的下一个节点指向None
		self.__head = node  # 头文件指向node
		node.next.prev = node #

	def append(self, item):
		"""链表尾部添加元素"""
		# item 只是具体的数据，不是节点，插入，
		# 要找到最后一个节点，插入数据
		node = Node (item)
		if self.is_empty ():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			cur.prev = cur # 前部节点指向前一个块

	def insert(self, pos, item):
		"""指定位置添加元素,pos 插入元素位置
		:param pos 从0开始
		"""
		if pos <= 0:
			self.add (item)
		elif pos > (self.length () - 1):
			"""不能包含等号"""
			pre = self.__head
			self.append (item)
		else:
			cur = self.__head
			count = 0
			while count <= pos:
				count += 1
				cur = cur.next
			# 当循环退出之后
			node = Node (item)
			node.next = cur
			node.prev = cur.prev
			cur.prev.next = node
			cur.prev = node

	def remove(self, item):
		"""删除节点
		直接删除对应的值，所以需要先遍历
		思路：删除后，就是删除元素的游标，前一个元素的游标指向，删除元素后一个游标
		"""
		cur = self.__head  # 第一个游标，指向第一位
		while cur != None:
			if cur.elem == item:
				# 先判断此节点是否是头节点
				# 头节点
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						# 判断链表是否只有一个元素
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
					break
			else:
				cur = cur.next
		pass

	def search(self, item):
		"""查找节点是否存在"""
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				# 判断当前值是否是要查找的值
				return True
			else:
				cur = cur.next
		return False


if __name__ == "__main__":
	dll = Dpuble_link_list()
	dll.append(1)
	print(dll.is_empty())
	print(dll.length())

	dll.append(2)
	print(dll.is_empty())
	print(dll.length())

	dll.append(3)
	dll.append(4)
	dll.append(5)
	dll.append(6)

	dll.travel()
	dll.insert(3,99)
	dll.remove(3)
	dll.travel()
	print(dll.length())
