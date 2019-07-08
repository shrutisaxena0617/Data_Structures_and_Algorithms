class MinStack:
  def __init__(self):
    self.mystack = []
    self.min_stack = []
  def push(self, elem):
    if self.isEmpty():
      self.min_stack.append(elem)
    else:
      if elem < self.min_stack[-1]:
        self.min_stack.append(elem)
    self.mystack.append(elem)
    print(self.min_stack)
  def pop(self):
    if self.isEmpty():
      return 'Stack is empty!!'
    else:
      popped = self.mystack.pop()
      if popped == self.min_stack[-1]:
        self.min_stack.pop()
      return popped
  def peek(self):
    if self.isEmpty():
      return 'Stack is empty!!'
    else:
      return self.mystack[-1]
  def isEmpty(self):
    return len(self.mystack) == 0
  def findMin(self):
    if len(self.min_stack) > 0:
      return self.min_stack[-1]

min_s = MinStack()
min_s.push(1)
min_s.push(20)
min_s.push(0)
min_s.push(5)
print(min_s.peek())
print(min_s.findMin())
