###### Basic queue implementation ######

# Queue Class

class Queue():
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    def enqueue(self,elem):
        self.queue.insert(0,elem)

    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.queue.pop()

    def display(self):
        for i in self.queue:
            print i,

# Implementation

queue = Queue()
print ('Enter queue elements separated by space :: ')
user_input = raw_input().split()

for i in user_input:
    queue.enqueue(int(i))

print ('Displaying original queue')
queue.display()

de = queue.dequeue()
print ('Dequeued element ' + str(de))

print ('Displaying queue after dequeue')
queue.display()


