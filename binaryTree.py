class TreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.left = left
		self.right = right
		self.data = data

	def insertData(self, value):
		self.data = value

	def getData(self):
		return self.data

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def traverse(self):
		print self.getData()
		if self.left != None:
			self.left.traverse()
		if self.right != None:
			self.right.traverse()

	def addNode(self, data, path):
		if path == '':
			self.insertData(data)
			return
		temp = TreeNode()
		if path[0] == '0':
			if self.left == None:
				self.left = temp
			self.left.addNode(data, path[1:])
		if path[0] == '1':
			if self.right == None:
				self.right = temp
			self.right.addNode(data, path[1:])

	#def pre_traverse(self):
		#print self.getData()
		#if self.left != None:
			#self.left.pre_traverse()
		#if self.right != None:
			#self.right.pre_traverse()

	#def in_traverse(self):
		#if self.left != None:
			#self.left.in_traverse()
		#print self.getData()
		#if self.right != None:
			#self.right.in_traverse()
		

class Tree:
	def __init__(self, node=None):
		self.head = node

	def traverse(self):
		self.head.traverse()

	def addNode(self, data, path):
		self.head.addNode(data, path)

	#def pre_traverse(self):
		#self.head.pre_traverse()

	#def in_traverse(self):
		#self.head.in_traverse()

if __name__ == '__main__':
	ary = [[1, ''], [2, '0'], [3, '1'], [4, '01'], [5, '10'], [6, '010']]
	tree = Tree(TreeNode())
	for i in ary:
		tree.addNode(i[0], i[1])
	tree.traverse()

