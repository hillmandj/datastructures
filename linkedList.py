
class Node:
	def __init__(self, data, ptr):
		self.data = data
		self.ptr = ptr

	def getData(self):
		return str(self.data)

	def getNext(self):
		return self.ptr

	def setData(self, value):
		self.data = value

	def setNext(self, new_ptr):
		self.ptr = new_ptr

class linkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insertBeginning2(self, data):
		temp_node = Node(data, self.head)
		if self.head == None:
			self.head = temp_node
			self.tail = temp_node
		else:
			self.head = temp_node

	def insertEnd2(self, data):
		temp_node = Node(data, None)
		if self.head == None:
			self.head = temp_node
			self.tail = temp_node
		else:
			self.tail.setNext(temp_node)
			self.tail = temp_node

	#the methods below are less efficient, but kept for reference.

	# def insertEnd(self, data):
	# 	temp_node = Node(data, None)
	# 	if self.head == None:
	# 		self.head = temp_node
	# 		self.tail = temp_node
	# 	elif self.head == self.tail:
	# 		self.tail = temp_node
	# 		self.head.setNext(self.tail)
	# 	else:
	# 		self.tail.setNext(temp_node)
	# 		self.tail = self.tail.getNext()

	# def insertBeginning(self, data):
	# 	''' 
	# 	insert a node at the beginning
	# 	be sure to think of the three cases: an empty list, a list with one element, and a list with multiple elements
	# 	run prn and insertEnd after you insert at the beginning, to ensure you didnt mess up your head node and tail node
	# 	'''    
	# 	temp_node = Node(data, None)
	# 	if self.head == None:
	# 		self.head = temp_node
	# 		self.tail = temp_node
	# 	elif self.head == self.tail:
	# 		self.head = temp_node
	# 		self.head.setNext(self.tail)
	# 	else:
	# 		temp_node.setNext(self.head)
	# 		self.head = temp_node

	def reverse_it(self):
		current_node = self.head
		reversed_head_node = None
		temp = None
		while current_node != None:
			temp = current_node.getNext()
			current_node.setNext(reversed_head_node)
			reversed_head_node = current_node
			current_node = temp
			self.head = reversed_head_node

	def prn(self):
		current_node = self.head
		while current_node != None:
			print 'this is current_node\'s data: ' + str(current_node.getData())
			current_node = current_node.getNext()



if __name__ == '__main__':
	L = linkedList()
	for i in range(2, 10, 2):
		L.insertEnd2(i)
	L.prn()
	print
	L.reverse_it()
	print
	L.prn()



