class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  def removeDuplicate(self):
    if self.head is None:
      return
    else:
      mydict = {}
      cur = self.head
      prev = None
      while cur:
        if mydict.get(cur.data, -1) == -1:
          mydict[cur.data] = cur.data
          prev = cur
          cur = cur.next
        else:
          if prev and cur:
            prev.next = cur.next
            cur = cur.next
          # else:
          #   self.head = cur.next # Why is this needed?
  def display(self):
    cur = self.head
    while cur:
      print(cur.data)
      cur = cur.next

llist = LinkedList()
llist.push(10)
llist.push(30)
llist.push(20)
llist.push(20)
llist.push(10)
llist.push(30)
print('Actual')
llist.display()
llist.removeDuplicate()
print('After removal')
llist.display()
