class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class LLNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def push(self, data):
    new_node = LLNode(data)
    new_node.next = self.head
    self.head = new_node

def inorder(root):
  if root:
    if root.left:
      inorder(root.left)
    print(root.data)
    if root.right:
      inorder(root.right)

def levelLL(root):
  if root:
    myqueue = []
    myqueue.insert(0, root)
    llist = LinkedList()
    llist.push(root.data)
    while len(myqueue) > 0:
      print(myqueue[-1].data)
      llist
      root = myqueue.pop()
      if root.left:
        myqueue.insert(0, root.left)
      if root.right:
        myqueue.insert(0, root.right)

root = Node(40)
root.left = Node(20)
root.right = Node(60)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(50)
root.right.right = Node(70)
print('display tree')
inorder(root)
print('level tree')
levelLL(root)
