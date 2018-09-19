# coding=utf-8 
# @Time : 2018/9/19 15:55 
# @Author : achjiang
# @File : code03_single_cycle_link_list.py

class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingleCycleLinkList(object):
	"""单链表"""
	def __init__(self, node=None):
		"""初始化，链表初始指向位置为空"""
		self.__head = node # 私有变量是双下滑线
	def is_empty(self):
		"""链表是否为空"""
		return self.__head == None

	def length(self):
		"""链表长度"""
		if self.is_empty():
			return 0
		# cur游标，用来移动遍历节点
		cur = self.__head
		# count记录数量
		count = 1
		while cur.next != self.__head:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur.next != self.__head:
			print(cur.elem, end=" ") # 打印cur.elem??
			cur = cur.next
		# 	退出循环时，cur指向结尾，但结尾元素未打印
		print(cur.elem) # 打印最后

	def add(self, item):
		"""链表头部添加元素"""
		node = Node(item) # 实例化为一个节点数据
		if self.is_empty():
			self.__head = node
			node.next = node
		# 因为是单向循环列表，所以需要遍历找到最后一个，
		cur = self.__head
		while cur.next != self.__head:
			cur = cur.next
		# 退出循环：
		node.next = self.__head # 将新节点的下一个节点指向None
		self.__head = node # 头文件指向node
		cur.next = self.__head # 指向投节点

	def append(self, item):
		"""链表尾部添加元素"""
		# item 只是具体的数据，不是节点，插入，
		# 要找到最后一个节点，插入数据
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			node.next = self.__head
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
		if self.is_empty():
			return
		cur = self.__head # 第一个游标，指向第一位
		pre = None # 第二个游标先命名为空
		while cur.next != self.__head:
			if cur.elem == item:
				# 先判断此节点是否是头节点
				# 头节点
				if cur == self.__head:
					# 头文件找尾节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else:
					# 中间节点
					pre.next = cur.next
				# break 不能使用break因为下面的实际还是在运行的
				return
			else:
				pre = cur
				cur = cur.next
		# 退出循环，cur指向尾节点
		# 即只有一个节点
		if cur.elem == item:
			if cur is self.__head:
				# 列表只有一个节点
				self.__head = None
			else:
				pre.next = cur.next


			pre.next = cur.next
		pass

	def search(self, item):
		"""查找节点是否存在"""
		if self.is_empty():
			return False
		cur = self.__head
		while cur.next != self.__head:
			if cur.elem == item:
				# 判断当前值是否是要查找的值
				return True
			else:
				cur = cur.next
		if cur.elem == item:
			# 如果一开始就查找成功就返回True
			return True
		return False

if __name__ == "__main__":
	ll = SingleCycleLinkList()
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