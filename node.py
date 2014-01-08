class Node:
	def __init__(self, data, ptr):
		self.data = data
		self.ptr = ptr
		
	def prn(self):
		print self.data
		
	def getData(self):
		return self.data
				
	def getNext(self):
		return self.ptr

	def setValue(self, value):
		self.data = value

	def setNext(self, new_ptr):
		self.ptr = new_ptr

if __name__ == '__main__':
	ary = [1,2, 3, 4, 5, 6]

	head_node = Node(ary[0], None)
	current_node = head_node
	for i in range(1,len(ary)):
		temp_node = Node(ary[i], None)
		current_node.setNext(temp_node)
		current_node = current_node.getNext()

	#print data
	current_node = head_node
	while current_node != None:
		print current_node.getData()
		current_node = current_node.getNext()






