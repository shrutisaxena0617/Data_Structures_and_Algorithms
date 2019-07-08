class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, data):
    if root is None or root.data == data:
        return root
    if data < root.data:
        return search(root.left, data)
    return search(root.right, data)

def insert(root, node):
    if root is None:
        root = node
    if node.data < root.data:
        if root.left:
            insert(root.left, node)
        else:
            root.left = node
    if node.data > root.data:
        if root.right:
            insert(root.right, node)
        else:
            root.right = node

def inorder(root):
    if root:
        if root.left:
            inorder(root.left)
        print(root.data)
        if root.right:
            inorder(root.right)

def minValue(root):
    cur = root
    while cur.left:
        cur = cur.left
    return cur.data

def maxValue(root):
    cur = root
    while cur.right:
        cur = cur.right
    return cur.data

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
print(search(root, 20))
new_node = Node(25)
insert(root, new_node)
inorder(root)
print('minvalue', minValue(root))
print('maxvalue', maxValue(root))
