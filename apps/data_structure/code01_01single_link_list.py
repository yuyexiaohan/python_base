# coding=utf-8 
# @Time : 2018/9/19 11:25 
# @Author : achjiang
# @File : code01_01single_link_list.py

# python 实现单链表

class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingLeLinkList(object):
	"""单链表"""
	def __init__(self, node=None):
		"""初始化，链表初始指向位置为空"""
		self.__head = node # 私有变量是双下滑线
	def is_empty(self):
		"""链表是否为空"""
		return self.__head == None

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
			print(cur.elem, end=" ") # 打印cur.elem??
			cur = cur.next

	def add(self, item):
		"""链表头部添加元素"""
		node = Node(item) # 实例化为一个节点数据
		node.next = self.__head # 将新节点的下一个节点指向None
		self.__head = node # 头文件指向node

	def append(self, item):
		"""链表尾部添加元素"""
		# item 只是具体的数据，不是节点，插入，
		# 要找到最后一个节点，插入数据
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		"""指定位置添加元素,pos 插入元素位置
		:param pos 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			"""不能包含等号"""
			pre = self.__head
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count <= (pos - 1):
				count += 1
				pre = pre.next
			# 当循环退出之后
			node = Node(item)
			node.next = pre.next
			pre.next = node



	def remove(self, item):
		"""删除节点
		直接删除对应的值，所以需要先遍历
		思路：删除后，就是删除元素的游标，前一个元素的游标指向，删除元素后一个游标
		"""
		cur = self.__head # 第一个游标，指向第一位
		pre = None # 第二个游标先命名为空
		while cur != None:
			if cur.elem == item:
				# 先判断此节点是否是头节点
				# 头节点
				if cur == self.__head:
					self.__head = cur.next
				else:
					pre.next = cur.next
					break
			else:
				pre = cur
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
	ll = SingLeLinkList()
	print(ll.is_empty())
	print(ll.length())

	ll.append(1)
	print(ll.is_empty())
	print(ll.length())

	ll.append(2)
	ll.add(8)

	# ll.insert(2,"ff")
	ll.append(3)
	ll.append(4)
	ll.append(5)
	ll.travel()
	print ("链表长度：", ll.length ())
	ll.insert(5,99)
	ll.insert(-1,-1)
	ll.insert(100,100)
	print()
	ll.travel()
	ll.remove(100)
	ll.travel()
	print()
	print(ll.search(99))
	print("链表长度：",ll.length())

"""
打印结果：
True
0
False
1
8 1 2 3 4 5 链表长度： 6

-1 8 1 2 3 4 5 99 100 -1 8 1 2 3 4 5 99 
True
链表长度： 8
"""