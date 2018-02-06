# Program to implement binary tree bu using Java Code in Robert Lafore book as reference and converting it to Python

class Node:
    def __init__(self, iData = None, data = None):
        self.iData = iData
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def display(self,id):
        pass

class BinaryTree:
    def __init__(self):
        self.root = Node()
    def insert(self, id, data):
        newNode = Node()
        newNode.iData = id
        newNode.data = data
        #print ('newNode ' + str(newNode.iData))
        if(self.root.iData == None):
            self.root = newNode
            #print self.root.iData
        else:
            current = self.root
            parent = Node()
            while(True):
                parent = current
                if(id < current.iData):
                    current = current.leftChild
                    if(current == None):
                        parent.leftChild = newNode
                        return
                else:
                    current = current.rightChild
                    if(current == None):
                        parent.rightChild = newNode
                        return
    def search(self, id):
        current = self.root
        print current
        print ('current.idata ' + str(current.iData))
        while not(current.iData == None):
            print ('Inside while')
            if(id < current.iData):
                current = current.leftChild
            else:
                current = current.rightChild
            if(current == None):
                print ('Inside if')
                return None
        print ('current.idata ' + str(current.iData))
        return current.iData
    def delete(self, id):
        pass

#implementation
tree = BinaryTree()
print tree
print tree.root
tree.insert(1,10)
print tree.root.iData
print tree.root.data
x=tree.search(1)
print x




