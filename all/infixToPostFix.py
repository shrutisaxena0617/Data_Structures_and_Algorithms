class Solution:
  def __init__(self, capacity):
    self.capacity = capacity
    self.top = -1
    self.mystack = []
    self.precedence = {'^':3, '*':2, '/':2, '+':1, '-':1}
    self.output = []
  def isEmpty(self):
    return self.top == -1
  def push(self, elem):
    self.top += 1
    self.mystack.append(elem)
  def pop(self):
    if not self.isEmpty():
      self.top -= 1
      return self.mystack.pop()
    else:
      return -1
  def peek(self):
    if not self.isEmpty():
      return self.mystack[-1]
    else:
      return -1
  def isOperand(self, ch):
    return ch.isalpha()
  def isNotGreater(self, i):
    try:
        a = self.precedence[i]
        b = self.precedence[self.peek()]
        return True if a <= b else False
    except KeyError:
        return False
  def infixToPostfix(self, exp):
      for e in exp:
        if self.isOperand(e):
          self.output.append(e)
        elif e == '(':
          self.push('(')
        elif e == ')':
          while not self.isEmpty() and self.peek() != '(':
            self.output.append(self.pop())
          if not self.isEmpty() and self.peek() != '(':
            return -1
          else:
            self.pop()
        else:
          while not self.isEmpty() and self.isNotGreater(e):
            self.output.append(self.pop())
          self.push(e)
      while not self.isEmpty():
        self.output.append(self.pop())
      #print(self.output)
      print (''.join(self.output))

# exp = "a+b*(c^d-e)^(f+g*h)-i"
exp = 'a+b*(c^d-e)^(f+g*h)-i'
s = Solution(len(exp))
s.infixToPostfix(exp)
