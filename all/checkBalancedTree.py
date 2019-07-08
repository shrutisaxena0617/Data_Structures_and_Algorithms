class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def depth(root):
  if root is None:
    return 0
  return 1 + max(depth(root.left), depth(root.right))

def depthNode(root):
  if root is None:
    return True
  return abs(depth(root.left) - depth(root.right)) <= 1

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
print(depthNode(root))
