class Node:
	def __init__(self, value):
		self.value = value
		self.nextval = None

class LinkedList:
	def __init__(self):
		self.headval = None 

	def append(self):
		printval = self.headval
		while printval is not None:
		    print (printval.value)
		    printval = printval.nextval

list = LinkedList()
list.headval = Node(" 1 ")
N2 = Node(" 2 ")
N3 = Node(" 3 ")
N4 = Node(" 4 ")

list.headval.nextval = N2

N2.nextval = N3
N3.nextval = N4

list.append()
