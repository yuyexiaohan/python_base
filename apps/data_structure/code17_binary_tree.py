# coding=utf-8 
# @Time : 2018/9/20 14:12 
# @Author : achjiang
# @File : code17_binary_tree.py

# 二叉树实现
class Node(object):
	"""节点构造"""
	def __init__(self, item):
		self.elem = item
		self.lchild = None
		self.rchild = None

class Tree(object):
	"""二叉树"""
	def __init__(self):
		self.root = None

	def add(self,item):
		"""添加"""
		node = Node(item) # 实例化一个节点
		if self.root is None:
			self.root = node
			return
		queue = [self.root]
		while queue:
			cur_node = queue.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queue.append(cur_node.lchild)
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:
				queue.append(cur_node.rchild)

	def breadth_travel(self):
		"""广度遍历"""
		if self.root is Node:
			return
		queue = [self.root]
		while queue:
			cur_node = queue.pop(0)
			print(cur_node.elem, end=" ")
			if cur_node.lchild is not None:
				queue.append(cur_node.lchild)
			if cur_node.rchild is not None:
				queue.append(cur_node.rchild)

	def preorder(self,node):
		"""先序遍历/层次遍历"""
		if node is None:
			return
		print(node.elem, end=" ")
		self.preorder(node.lchild)
		self.preorder(node.rchild)

	def inorder(self,node):
		"""先中序遍历"""
		if node is None:
			return
		self.inorder(node.lchild)
		print(node.elem, end=" ")
		self.inorder(node.rchild)

	def postorder(self,node):
		"""后序遍历"""
		if node is None:
			return
		self.postorder(node.lchild)
		self.postorder(node.rchild)
		print(node.elem, end=" ")


if __name__ == "__main__":
	tree = Tree()
	tree.add(0)
	tree.add(1)
	tree.add(2)
	tree.add(3)
	tree.add(4)
	tree.add(5)
	tree.add(6)
	tree.add(7)
	tree.add(8)
	tree.add(9)
	tree.breadth_travel()
	print('')
	tree.preorder(tree.root)
	print('')
	tree.inorder(tree.root)
	print('')
	tree.postorder(tree.root)

"""
打印结果：
# 1. 层次遍历/广度遍历：先上层，再下层
1 2 3 4 5 6 7 8 9
# 2. 先序遍历：先根，再左，再右
1 2 4 8 9 5 3 6 7 
# 3.中序遍历：先左，再根，再右
7 3 8 1 9 4 0 5 2 6 
# 4. 后序遍历：先左，再右，再根
7 8 3 9 4 1 5 6 2 0
"""