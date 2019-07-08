class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class myStack:
    def __init__(self):
        self.head = None
    def push(self, elem):
        new_node = Node(elem)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if not self.isEmpty():
            temp = self.head
            self.head = self.head.next
            popped = temp.data
            return popped
    def peek(self):
        if not self.isEmpty():
            return self.head.data
    def display(self):
        if not self.isEmpty():
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next
    def isEmpty(self):
        if self.head is None:
            return True
        return False

sol = myStack()
sol.push(10)
sol.push(20)
sol.push(30)
sol.push(40)
sol.display()
print(sol.peek())
print('pop', sol.pop())
sol.display()
