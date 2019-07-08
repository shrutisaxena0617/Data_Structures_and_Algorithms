class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def checkBST(root):
  return checkBSTHelp(root, -float('INF'), float('INF'))

def checkBSTHelp(root, min_val, max_val):
  if root is None:
    return True
  if root.data < min_val or root.data > max_val:
    return False
  return checkBSTHelp(root.left, min_val, root.data-1) and checkBSTHelp(root.right, root.data+1, max_val)


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
print(checkBST(root))
