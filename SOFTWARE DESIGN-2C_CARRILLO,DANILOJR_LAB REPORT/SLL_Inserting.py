
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
      
class SLinkedList:
   def __init__(self):
      self.headval = None

   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
         

list = SLinkedList()
list.headval = Node("First")
e2 = Node("Third")
e3 = Node("Last")
list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Second")

list.listprint()