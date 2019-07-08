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
  def display(self):
    if self.head:
      cur = self.head
      while cur:
        print(cur.data)
        cur = cur.next
  def findIntersection(self, head1, head2):
    if head1 and head2:
      last1, len1 = self.findLastNode(head1)
      last2, len2 = self.findLastNode(head2)
      if last1 != last2:
        return
      diff = abs(len1 - len2)
      cur1 = head1
      cur2 = head2
      # print(cur1.data)
      # print(cur2.data)
      # print (diff)
      ctr = 0
      if diff > 0:
        if len1 > len2:
          while cur1 and ctr < diff:
            ctr += 1
            cur1 = cur1.next
        else:
          while cur2 and ctr < diff:
            ctr += 1
            cur2 = cur2.next
      # print(cur1.data)
      # print(cur2.data)
      while cur1 and cur2:
        if cur1.data == cur2.data:
            return cur1.data
        cur1 = cur1.next
        cur2 = cur2.next

  def findLastNode(self, head):
    size = 0
    while head:
      size += 1
      head = head.next
    return head, size

llist1 = LinkedList()
llist1.push(50)
llist1.push(40)
llist1.push(30)
llist1.push(20)
llist1.push(10)
llist1.display()
print('list2')
llist2 = LinkedList()
llist2.push(50)
llist2.push(10)
llist2.push(10)
llist2.push(10)
llist2.push(0)
llist2.push(-1)
llist2.push(-2)
llist2.display()
print('intersection node')
res = llist2.findIntersection(llist1.head, llist2.head)
print(res)
