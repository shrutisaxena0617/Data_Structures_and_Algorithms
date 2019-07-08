class StackArray:
  def __init__(self):
    self.mystack = []
  def isEmpty(self):
    return self.mystack == []
  def push(self, elem):
    self.mystack.append(elem)
  def pop(self):
    if not self.isEmpty():
      self.mystack.pop()
  def peek(self):
    if not self.isEmpty():
      return self.mystack[-1]
  def display(self):
    for i in self.mystack:
      print(i)

mystack = StackArray()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
print('Printing stack')
mystack.display()
print('Peeked element')
print(mystack.peek())
mystack.pop()
print('Post pop')
mystack.display()
