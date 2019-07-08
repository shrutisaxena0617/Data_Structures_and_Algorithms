class Solution:
    def __init__(self, size):
        self.arr = []
        self.size = size
    def insert(self, elem):
        if self.isEmpty():
            self.arr[0] = elem
            self.size += 1
            return 'Inserted record successfully'
        if not self.isFull():
            self.arr.insert(0, elem)
            self.size += 1
            return 'Inserted record successfully'
        else:
            return 'Array already full!!'
    def push(self, elem):
        if not self.isFull():
            self.arr.append(elem)
            self.size += 1
            return 'Inserted record successfully'
        else:
            return 'Array already full!!'
    def insertAfter(self, which_elem, elem):
        if not self.isFull():
            pos = self.search(which_elem)
            self.arr.insert(pos+1, elem)
            self.size += 1
            return 'Inserted record successfully'
        else:
            return 'Array already full!!'
    def search(self, elem):
        if not self.isEmpty():
            return self._binary_search(0, len(self.arr)-1, self.arr, elem)
        else:
            return -1
    def _binary_search(self, l, r, arr, elem):
        while l <= r:
            mid = int(l + (r-1)/2)
            if arr[mid] == elem:
                return mid
            elif arr[mid] > elem:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    def update(self, elem, new_elem):
        if self.isEmpty():
            return -1
        else:
            pos = self.search(elem)
            self.arr[pos] = new_elem
            return ('Updated successfully!')
    def delete(self, elem):
        if self.isEmpty():
            return -1
        else:
            pos = self.search(elem)
            self.arr.pop(pos)
            return ('Deleted successfully!')
    def display(self):
        for i in self.arr:
            print(i)
    def isEmpty(self):
        return len(self.arr) == 0
    def isFull(self):
        return len(self.arr) == self.size

sol = Solution(10)
sol.push(20)
sol.push(30)
sol.push(50)
sol.insert(10)
sol.display()
sol.insertAfter(30,40)
sol.display()
sol.update(50,60)
sol.display()
sol.delete(60)
sol.display()
