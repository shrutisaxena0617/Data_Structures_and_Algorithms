class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None

def connectNodes(root):
  if root is None:
    return
  connectNodesHelp(root.left, root.right)

def connectNodesHelp(left, right):
  if left is None and right is None:
    return
  left.next = right
  connectNodesHelp(left.left, left.right)
  connectNodesHelp(left.right, right.left)
  connectNodesHelp(right.left, right.right)
