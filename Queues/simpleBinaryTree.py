class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, data):
        if(self.root):
            self._put(data, self.root)
        else:
            self.root = Node(data)

    def _put(self, data, currentNode):
        if(data < currentNode.data):
            if(currentNode.left):
                self._put(data, currentNode.left)
            else:
                currentNode.left = Node(data)
        else:
            if(currentNode.right):
                self._put(data, currentNode.right)
            else:
                currentNode.right = Node(data)

    def inorder(self):
        if(self.root):
            self._inorder(self.root)

    def _inorder(self, currentNode):
        if(currentNode.left):
            self._inorder(currentNode.left)
        print currentNode.data
        if(currentNode.right):
            self._inorder(currentNode.right)

    def breadthfirstsearch(self):
        if(self.root):
            self._breadthfirstsearch(self.root)

    def _breadthfirstsearch(self, currentNode):
        if(currentNode == None):
            return None
        else:
            myqueue = []
            myqueue.append(currentNode)
            while (len(myqueue) > 0):
                print myqueue[0].data
                currentNode = myqueue.pop(0)
                if(currentNode.left):
                    myqueue.append(currentNode.left)
                if(currentNode.right):
                    myqueue.append(currentNode.right)

    def maxDepth(self):
        if(self.root):
            maxDepth = self._maxDepth(self.root)
            return maxDepth

    def _maxDepth(self, currentNode):
        if(currentNode == None):
            return 0
        else:
            lDepth = self._maxDepth(currentNode.left)
            rDepth = self._maxDepth(currentNode.right)
            if(lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def diameter(self):
        if(self.root):
            diameter = self._diameter(self.root)
            return diameter

    def _diameter(self, currentNode):
        if(currentNode == None):
            #print ('Inside if')
            return 0
        else:
            #print ('Inside else')
            lPoint = self._diameter(currentNode.left)
            #print lPoint
            rPoint = self._diameter(currentNode.right)
            #print rPoint
            return (lPoint+rPoint+1)

mytree = BinarySearchTree()
mytree.put(10)
mytree.put(2)
mytree.put(22)
mytree.put(15)
mytree.put(70)
mytree.put(100)
mytree.put(92)
mytree.put(56)
mytree.inorder()
print('Breadth First Search')
mytree.breadthfirstsearch()
print ('Max Depth of tree')
print mytree.maxDepth()
print ('Diameter of tree')
print mytree.diameter()