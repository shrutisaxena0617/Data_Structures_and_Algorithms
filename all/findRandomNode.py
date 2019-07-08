import random
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def findRandomNode(root):
  arr = []
  inorder(root, arr)
  print(arr[random.randint(0, len(arr))])

def inorder(root, arr):
  if root:
    if root.left:
      inorder(root.left, arr)
    arr.append(root.data)
    if root.right:
      inorder(root.right, arr)
  else:
    return None

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
findRandomNode(root)
