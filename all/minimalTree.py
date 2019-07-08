class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inorder(root):
  if root:
    if root.left:
      inorder(root.left)
    print(root.data)
    if root.right:
      inorder(root.right)

def minimalTree(arr):
    if arr:
        mid = len(arr)//2
        root = Node(arr[mid])
        root.left = minimalTree(arr[:mid])
        root.right = minimalTree(arr[mid+1:])
        return root

res = minimalTree([1,2,3,4,5,6])
#minimalTree([1,2,3,4,5,6])
inorder(res)
