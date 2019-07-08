class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def append(self, node):
    if self.head is None:
      self.head = node
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = node
  def display(self, head):
    if head:
      temp = head
      while temp:
        print(temp.val)
        temp = temp.next

def breadthFirstSearchLL(root):
  if not root:
    return []
  res = []
  myqueue = []
  myqueue.insert(0, root)
  llist = LinkedList()
  llist.append(root)
  res.append(root)
  while len(myqueue) > 0:
    n = len(myqueue)
    temp = LinkedList()
    for i in range(n):
      root = myqueue.pop()
      if root.left:
        myqueue.insert(0, root.left)
        temp.append(root.left)
      if root.right:
        myqueue.insert(0, root.right)
        temp.append(root.right)
    if temp.head is not None:
      res.append(temp.head)
  return res

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(15)
root.left.right = Node(25)
root.right.left = Node(27)
root.right.right = Node(35)
res = breadthFirstSearchLL(root)
llist = LinkedList()
for i in range(len(res)):
    print('level', i)
    llist.display(res[i])
