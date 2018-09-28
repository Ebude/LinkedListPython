#Creating a node (element) of the list and its pointer
class Node:
  def __init__(self, dataval=None):
    self.dataval=dataval
    self.nextval=None

#Creating the list
class LinkedList:
  def __init__(self):
    self.headval=None
    
#Print list function
  def PrintList(self):
    printval=self.headval
    while printval is not None:
      print(printval.dataval)
      printval=printval.nextval

#Insert List
# a) At the begining
  def AtBegining(self,data):
    newnode=Node(data)
    newnode.nextval=self.headval
    self.headval=newnode
# b) At the end
  def AtEnd(self, data):
    newnode=Node(data)
    lastval=self.headval
    if lastval.dataval==None:
      self.headval=newnode
      return
    while lastval.nextval is not None:
      lastval=lastval.nextval
    lastval.nextval=newnode
# c) Inbetween
  def InBetween(self,node,data):
    newnode=Node(data)
    newnode.nextval=node.nextval
    node.nextval=newnode

    
##Delete a item in list
  def DeleteItem(self,item):
    node=Node(item)
    deleteval=self.headval
    if self.headval.dataval==node.dataval:
      self.headval = self.headval.nextval
      return
    prev=self.headval
    while deleteval is not None:
      if deleteval.dataval==item:
        break
      prev =deleteval
      deleteval=deleteval.nextval
    prev.nextval=deleteval.nextval
    
    
    

#Creating the nodes
Months=LinkedList()
Months.headval=Node('January')
n2=Node('February')
n3=Node('March')
n4=Node('April')

#Linking the nodes
Months.headval.nextval=n2
n2.nextval=n3
n3.nextval=n4

#print list
Months.PrintList()

print("###################################")

#Print with changes
Months.AtBegining('Months of the Year')
Months.AtEnd('The End')
Months.InBetween(n2,'The month with the least days')
Months.PrintList()

print("###################################")

#Delet an item
Months.DeleteItem('Months of the Year')
Months.PrintList()
