class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root:
        if root.left:
            inOrder(root.left)
        print(root.data)
        if root.right:
            inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data)
        if root.left:
            preOrder(root.left)
        if root.right:
            preOrder(root.right)

def postOrder(root):
    if root:
        if root.left:
            postOrder(root.left)
        if root.right:
            postOrder(root.right)
        print(root.data)

def breadthFirstSearch(cur):
    if not cur:
        return 0
    myqueue = []
    myqueue.insert(0, cur)
    while len(myqueue) > 0:
        print(myqueue[-1].data)
        cur = myqueue.pop()
        if cur.left:
            myqueue.insert(0, cur.left)
        if cur.right:
            myqueue.insert(0, cur.right)

def breadthFirstSearch_list(cur):
    if not cur:
        return []
    myqueue = []
    res = []
    myqueue.insert(0, cur)
    res.append([cur.data])
    while len(myqueue) > 0:
        n = len(myqueue)
        temp = []
        # print(myqueue[-1].data)
        for i in range(n):
            cur = myqueue.pop()
            if cur.left:
                myqueue.insert(0, cur.left)
                temp.append(cur.left.data)
            if cur.right:
                myqueue.insert(0, cur.right)
                temp.append(cur.right.data)
        if temp:
            res.append(temp)
    return res

def depth(cur):
    if not cur:
        return 0
    return 1 + max(depth(cur.left), depth(cur.right))

def diameter(cur):
    if not cur:
        return 0
    ldepth = depth(cur.left)
    rdepth = depth(cur.right)
    ldia = diameter(cur.left)
    rdia = diameter(cur.right)
    return max(1+ldepth+rdepth, max(ldia, rdia))

# def buildTree(inorder, preorder, start, end):
#     if start > end:
#         return
#     tNode = Node(preorder[buildTree.preIndex])
#     buildTree.preIndex += 1

def kDistant(root, k):
    if not root:
        return
    if k==0:
        print(root.data)
    else:
        kDistant(root.left, k-1)
        kDistant(root.right, k-1)

def printAncestors(root, target):
    if not root:
        return False
    if root.data == target:
        return True
    if printAncestors(root.left, target) or printAncestors(root.right, target):
        print (root.data)
        return True
    return False

def isIdentical(T, S):
    if S is None and T is None:
        return True
    if S is None or T is None:
        return False
    return T.data == S.data and isIdentical(T.left, S.left) and isIdentical(T.right, S.right)

def isSubtree(T, S):
    if S is None:
        return True
    if T is None:
        return False
    if isIdentical(T, S):
        return True
    return isSubtree(T.left, S) or isSubtree(T.right, S)

# def isSubtree(T,S):
#     if S is None:
#         return True
#     T_in, T_pre, S_in, S_pre = [], [], [], []
#     #T_in
#     if T.left:
#         T_in.append(T.left.data)
#     T_in.append(T.data)
#     if T.right:
#         T_in.append(T.right.data)
#     #T_pre
#     T_pre.append(T.data)
#     if T.left:
#         T_pre.append(T.left.data)
#     if T.right:
#         T_pre.append(T.right.data)
#     #S_in
#     if S.left:
#         S_in.append(S.left.data)
#     S_in.append(S.data)
#     if S.right:
#         S_in.append(S.right.data)
#     #S_pre
#     S_pre.append(S.data)
#     if S.left:
#         S_pre.append(S.left.data)
#     if S.right:
#         S_pre.append(S.right.data)
#     return set(S_pre).issubset(T_pre) and set(S_in).issubset(T_in)

# def isSubtree(T, S):
#     if S is None:
#         return True
#     if T is None:
#         return True
#     if identical(T,S):
#         return True
#     return isSubtree(T.left, S) or isSubtree(T.right, S)
#     #return False
#
# def identical(root1, root2):
#     if root1 is None and root2 is None:
#         return True
#     if root1 is None or root2 is None:
#         return False
#     return root1.data == root2.data and identical(root1.left, root2.left) and identical(root1.right, root2.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(15)
root.left.right = Node(25)
root.right.left = Node(27)
root.right.right = Node(35)
# print('Inorder')
# inOrder(root)
# print('Preorder')
# preOrder(root)
# print('Postorder')
# postOrder(root)
# print('Breadth First Search')
# breadthFirstSearch(root)
# print('Depth = ', depth(root))
# print('Diameter = ', diameter(root))
# # buildTree.preIndex = 0
# # inorder = []
# # preorder = []
# # root = buildTree(inorder, preorder, 0, len(inorder)-1)
# kDistant(root, 2)
# print('ancestors')
# printAncestors(root, 10)
# root_sub = Node(20)
# root_sub.left = Node(15)
# root_sub.right = Node(25)
# print(isSubtree(root, root_sub))
print(breadthFirstSearch_list(root))
