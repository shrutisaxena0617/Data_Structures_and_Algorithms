class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def kSumPaths(root, kSum):
  if root:
    paths = []
    path = []
    findPath(root, kSum, path, paths)
    print(paths)

def findPath(root, kSum, path, paths):
  if root is None:
    return False
  path.append(root.data)
  if kSum == sum(path):
    paths.append(path)
  if (root.left and findPath(root.left, kSum, path, paths)) or (root.right and findPath(root.right, kSum, path, paths)):
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
kSumPaths(root, 50)
