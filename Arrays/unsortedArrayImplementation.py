class Solution:
  def __init__(self):
    self.arr = []
  def isEmpty(self):
    return len(self.arr) == 0
  def insert(self, elem):
    self.arr.append(elem)
  def insertAt(self, elem, pos):
    self.arr.insert(pos, elem)
  def delete(self, elem):
    self.arr.remove(elem)
  def update(self, elem, newelem):
    for i in range(len(self.arr)):
      if self.arr[i] == elem:
        self.arr[i] = newelem
        return
  def search(self, elem):
    for i in range(len(self.arr)):
      if elem == self.arr[i]:
        return i
  def display(self):
    for i in self.arr:
      print(i)

sol = Solution()
sol.insert(10)
sol.insert(20)
sol.insert(30)
sol.display()
sol.delete(10)
sol.display()
sol.update(20,30)
sol.display()
sol.update(10,30)
sol.display()
