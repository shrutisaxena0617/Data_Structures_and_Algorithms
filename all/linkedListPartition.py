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

  def partition(self, node, elem):
    if not node:
      return
    head = node
    tail = node
    while node:
      next = node.next
      if node.data < elem:
        node.next = head
        head = node
      else:
        tail.next = node
        tail = node
      node = next
    tail.next = None
    return head

  def display(self, head):
    if head:
      while head:
        print(head.data)
        head = head.next

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(10)
llist.push(5)
llist.push(8)
llist.push(5)
llist.push(3)
llist.display(llist.head)
# print(llist.head)
new_head = llist.partition(llist.head, 5)
# print(new_head)
print('After partition')
llist.display(new_head)
