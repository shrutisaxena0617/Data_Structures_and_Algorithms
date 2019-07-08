class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLL:
  def __init__(self):
    self.last = None

  def insertWhenEmpty(self, data):
    new_node = Node(data)
    self.last = new_node
    new_node.next = new_node

  def insertAtBeginning(self, data):
    new_node = Node(data)
    new_node.next = self.last.next
    self.last.next = new_node

  def insertAtEnd(self, data):
    new_node = Node(data)
    new_node.next = self.last.next
    self.last.next = new_node
    self.last = new_node

  def insertBetween(self, data):
    pass

  def display(self):
    cur = self.last
    mydict = {}
    if cur is None:
      return
    while cur and cur not in mydict:
      print(cur.next.data)
      mydict[cur] = cur.data
      cur = cur.next

clist = CircularLL()
clist.insertWhenEmpty(10)
clist.insertAtBeginning(0)
clist.insertAtEnd(20)
clist.display()
