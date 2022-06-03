
# A single node of a singly linked list
class Node:
  def __init__(self, data, next=None):
	    self.data = data
	    self.next = next
 
# Creating a single node
first = Node("first")
second = Node("second")
print(first.data)
print(second.data)
