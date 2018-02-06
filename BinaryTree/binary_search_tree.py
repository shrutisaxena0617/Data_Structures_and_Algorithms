# Program to implement binary search tree (reference http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html)

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def len(self):
        return self.size

    def put(self, key, val):
        if(self.root):
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if (key < currentNode.key):
            if(currentNode.hasLeftChild()):
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if(currentNode.hasRightChild()):
                self._put(key, val, currentNode.rightChild)
                # Change condition here to include condition for duplicate value (Replace the existing to avoid duplicate values)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key):
        if(self.root):
            res = self._get(key, self.root)
            if(res):
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif(key == currentNode.key):
            return currentNode
        elif(key < currentNode.key):
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def getRoot(self):
        return self.root

    def preorder(self):
        myroot = self.getRoot()

        if(self.leftChild):
            self.leftChild.preorder()
        if(self.rightChild):
            self.rightChild.preorder()

    def postorder(self):
        if(self.leftChild):
            self.leftChild.postorder()
        if(self.rightChild):
            self.rightChild.postorder()
        print self.key

    def inorder(self):
        if(self.leftChild):
            self.leftChild.inorder()
        print self.key
        if(self.rightChild):
            self.rightChild.inorder()

class TreeNode:

    def __init__(self, key, val, lchild = None, rchild = None, parent = None):
        self.key = key
        self.value = val
        self.leftChild = lchild
        self.rightChild = rchild
        self.parent = parent

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def isLeftChild(self):
        return (self.parent and self.parent.leftChild == self)

    def isRightChild(self):
        return (self.parent and self.parent.rightChild == self)

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def hasAnyChildren(self):
        return (self.leftChild or self.rightChild)

    def hasBothChildren(self):
        return (self.leftChild and self.rightChild)

    def replaceNode(self, key, val, lchild, rchild):
        self.key = key
        self.value = val
        self.leftChild = lchild
        self.rightChild = rchild
        if(self.hasLeftChild()):
            self.leftChild.parent = self
        if(self.hasRightChild()):
            self.rightChild.parent = self


mytree = BinarySearchTree()
mytree.put(1,10)
mytree.put(2,20)
mytree.put(3,25)
print mytree.root
print mytree.len()
for i in range(1,4):
    print mytree.get(i)

print ('Preorder traversal')
mytree.preorder()
print ('Postorder traversal')
mytree.postorder()
print ('Inorder traversal')
mytree.inorder()