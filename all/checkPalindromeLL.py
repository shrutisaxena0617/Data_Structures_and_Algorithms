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
  def checkPalindrome(self):
    fast = self.head
    slow = self.head
    mystack = []
    while fast and slow and fast.next:
      mystack.append(slow.data)
      slow = slow.next
      fast = fast.next.next
    if fast:
      mystack.append(slow.data)
    while slow:
      if slow.data != mystack.pop():
        return False
      slow = slow.next
    return True

llist = LinkedList()
llist.push(10) #s,f
llist.push(20) #s
llist.push(30) #f, s
llist.push(30)
llist.push(20) #f
llist.push(10)
print(llist.checkPalindrome())
