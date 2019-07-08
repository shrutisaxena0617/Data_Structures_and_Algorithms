class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def findLowestCommonAncestor(root, node1, node2):
  path1, path2 = [], []
  if not findPath(root, node1.data, path1) or not findPath(root, node2.data, path2):
    return -1
  i = 0
  while i < len(path1) and i < len(path2):
    if path1[i] != path2[i]:
      break
    i += 1
  return path1[i-1]

def findPath(root, nodeData, path):
  if root is None:
    return False
  path.append(root.data)
  if root.data == nodeData:
    return True
  if (root.left and findPath(root.left, nodeData, path)) or (root.right and findPath(root.right, nodeData, path)):
    return True
  path.pop()
  return False

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(15)
root.left.right = Node(25)
root.right.left = Node(27)
root.right.right = Node(35)
print(findLowestCommonAncestor(root, root.left, root.right))
