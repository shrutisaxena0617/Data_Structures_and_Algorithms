class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLL:
  def __init__(self):
    self.head = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    if self.head is not None:
      self.head.prev = new_node
    self.head = new_node

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new_node
    new_node.prev = temp

  def insertAfter(self, somedata, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    temp = self.head
    while temp.next and temp.data != somedata:
      temp = temp.next
    new_node.next = temp.next
    new_node.prev = temp
    temp.next.prev = new_node
    temp.next = new_node

  def display(self):
    if self.head is None:
      return
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def delete(self, data):
    if self.head is None:
      return
    temp = self.head
    if temp.data == data:
        self.head = temp.next
        temp.next.prev = None
        return
    while temp and temp.data != data:
      temp = temp.next
    if temp is None:
        return -1
    if temp.next is None:
            temp.prev.next = None
            temp = None
            return
    temp.next.prev = temp.prev.next
    temp.prev.next = temp.next
    temp = None

  def reverse(self):
      cur = self.head
      prev_ptr = None
      while cur:
          prev_ptr = cur.prev
          cur.prev = cur.next
          cur.next = prev_ptr
          cur = cur.prev
      if prev_ptr is not None:
          self.head = prev_ptr.prev

dlist = DoublyLL()
dlist.push(30)
dlist.push(20)
dlist.push(10)
dlist.append(50)
dlist.insertAfter(30, 40)
dlist.display()
print('postdelete')
print(dlist.delete(50))
dlist.display()
print('postreverse')
dlist.reverse()
dlist.display()
