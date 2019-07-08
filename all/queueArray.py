class queueArray:
  def __init__(self, capacity):
    self.capacity = capacity
    self.rear = capacity - 1
    self.front = self.size = 0
    self.myqueue = [None]*self.capacity
  def isEmpty(self):
    return self.size == 0
  def isFull(self):
    return self.size == self.capacity
  def enqueue(self, elem):
    if self.isFull():
      return -1
    else:
      self.rear = (self.rear + 1) % self.capacity
      self.size += 1
      self.myqueue[self.rear] = elem
  def dequeue(self):
    if self.isEmpty():
      return -1
    else:
      self.front = (self.front + 1) % self.capacity
      self.size -= 1
  def queue_front(self):
    if self.isEmpty():
      return -1
    else:
      return self.myqueue[self.front]
  def queue_rear(self):
    if self.isEmpty():
      return -1
    else:
      return self.myqueue[self.rear]
  def display(self):
    for i in range(self.front, self.rear+1):
      print(self.myqueue[i])

q = queueArray(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.display()
