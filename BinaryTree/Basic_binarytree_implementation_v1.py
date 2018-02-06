class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, newNode):
        if(self.leftChild == None):
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self, newNode):
        if(self.rightChild == None):
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRootVal(self):
        return self.key
    def setRootVal(self, obj):
        self.key = obj
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def preorder(self):
        print self.key
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

tree = BinaryTree(10)
print tree.getRootVal()
tree.insertLeft(5)
tree.insertRight(15)
print tree.getLeftChild().getRootVal()
print tree.getRightChild().getRootVal()
print 'PreOrder'
tree.preorder()
print 'PostOrder'
tree.postorder()
print 'InOrder'
tree.inorder()