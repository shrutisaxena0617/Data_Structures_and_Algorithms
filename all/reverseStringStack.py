class StackArray:
  def __init__(self):
    self.mystack = []
  def isEmpty(self):
    return len(self.mystack) == 0
  def push(self, elem):
    self.mystack.append(elem)
  def pop(self):
    if not self.isEmpty():
      return self.mystack.pop()
  def display(self):
    for i in self.mystack:
      print(i)

# s = StackArray()
# x = 'shruti'
# x_list = list(x)
# for i in x_list:
#     s.push(i)
# s.display()
# res = []
# while not s.isEmpty():
#     res.append(s.pop())
# print(''.join(res))

s = StackArray()
x = 'shruti'
for i in x:
    s.push(i)
s.display()
res = []
while not s.isEmpty():
    res.append(s.pop())
print(''.join(res))
