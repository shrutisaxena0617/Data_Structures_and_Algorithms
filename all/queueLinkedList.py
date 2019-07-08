class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class myQueue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, data):
        temp = Node(data)
        if self.isEmpty():
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.front = self.front.next

    def display(self):
        if self.isEmpty():
            return
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

q = myQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.display()
