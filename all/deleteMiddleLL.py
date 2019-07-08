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
  def deleteMiddle(self):
    cur1 = self.head
    cur2 = self.head
    prev = None
    while cur1 and cur2 and cur2.next:
      prev = cur1
      cur1 = cur1.next
      cur2 = cur2.next.next
    if prev:
        prev.next = cur1.next
        cur1 = None
        return
    else:
        self.head = cur1.next
    # return cur1.data
  def display(self):
    cur = self.head
    while cur:
        print(cur.data)
        cur = cur.next

llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)
print('actual')
llist.display()
llist.deleteMiddle()
print('after deleting middle element')
llist.display()
