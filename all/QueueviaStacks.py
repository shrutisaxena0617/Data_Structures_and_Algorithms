class QueueViaStack:
  def __init__(self):
    self.mystack1 = []
    self.mystack2 = []

  def enqueue(self, data):
    self.mystack1.append(data)

  def dequeue(self):
    if self.mystack1:
      while len(self.mystack1) > 0:
        self.mystack2.append(self.mystack1.pop())
      popData = self.mystack2.pop()
      while len(self.mystack2) > 0:
        self.mystack1.append(self.mystack2.pop())
      return popData

  def display(self):
    if self.mystack1:
      for i in range(len(self.mystack1)-1, -1, -1):
        print(self.mystack1[i])

q = QueueViaStack()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print('Queue before pop')
q.display()
print(q.dequeue())
print('Queue after pop')
q.display()
