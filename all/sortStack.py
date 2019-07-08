class Stack:
  def __init__(self):
    self.sortStack = []
  def push(self, data):
    self.sortStack.append(data)
  def pop(self):
    if not self.isEmpty():
      return self.sortStack.pop()
  def isEmpty(self):
    return len(self.sortStack) == 0
  def sortMyStack(self):
    #if not self.isEmpty():
      bufferStack = []
      while not self.isEmpty():
        temp = self.pop()
        if bufferStack:
          while bufferStack and bufferStack[-1] > temp:
            self.push(bufferStack.pop())
        bufferStack.append(temp)
      #if bufferStack:
      while bufferStack:
        self.push(bufferStack.pop())
  def display(self):
    if not self.isEmpty():
      for i in range(len(self.sortStack)):
        print(self.sortStack[i])

s = Stack()
s.push(10)
s.push(30)
s.push(40)
s.push(20)
s.push(50)
print('original stack')
s.display()
s.sortMyStack()
print('sorted stack')
s.display()
