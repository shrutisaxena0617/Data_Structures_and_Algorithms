class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  # def returnKthLastNode(self, k):
  #   cur = self.head
  #   arr = []
  #   i = 0
  #   while cur:
  #     arr.append(cur.data)
  #     i += 1
  #     cur = cur.next
  #   return arr[-2]
  def returnKthLastNodeWithTwoPtrs(self, k):
    cur1 = self.head
    cur2 = self.head
    ctr = 0
    while ctr < k and cur2:
        cur2 = cur2.next
        ctr += 1
    while cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1.data

llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
# print(llist.returnKthLastNode(2)) #20
print(llist.returnKthLastNodeWithTwoPtrs(1))
