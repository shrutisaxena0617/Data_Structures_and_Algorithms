class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def push(self, data): #beginning
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  def insertAfter(self, prev_node, data): #insert after
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = prev_node.next
      prev_node.next = new_node
  def append(self, data): #end
    new_node = Node(data)
    last = self.head
    while(last.next):
      last = last.next
    last.next = new_node
  def display(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
  def delete(self, data):
      temp = self.head
      if temp is not None:
          if temp.data == data:
              self.head = temp.next
              temp = None
              return
      while temp is not None:
          if temp.data == data:
              break
          prev = temp
          temp = temp.next
      if temp is None:
          return
      prev.next = temp.next
      temp = None
  def deleteAt(self, pos):
      if self.head is None:
          return
      temp = self.head
      if pos == 0:
          self.head = temp.next
          temp = None
          return
      for i in range(pos-1):
          temp = temp.next
          if temp is None:
              break
      if temp is None or temp.next is None:
          return
      next = temp.next.next
      temp.next = None
      temp.next = next
  def len(self):
      if self.head is None:
          return 0
      temp = self.head
      count = 0
      while(temp):
          count += 1
          temp = temp.next
      return count
  def update_external_node(self, some_node, data):
      if self.head is not None:
          temp = self.head
          if temp.data == data:
              if temp.next is None:
                  some_node.next = None
                  self.head = some_node
              else:
                  some_node.next = temp.next
                  self.head = some_node
              return
          prev = None
          while temp.next:
              prev = temp
              temp = temp.next
              if temp.data == data:
                  break
          if temp.next is None:
              prev.next = some_node
              temp = None
          else:
              some_node.next = temp.next
              prev.next = some_node
              temp = None
  def swap_nodes(self, data1, data2):
      if self.head is None or data1 == data2 or not data1 or not data2:
          return
      prev1, cur1 = self.find_node(data1)
      prev2, cur2 = self.find_node(data2)
      if cur1 is None or cur2 is None:
          return
      if prev1 is not None:
          prev1.next = cur2
      else:
          self.head = cur2
      if prev2 is not None:
          prev2.next = cur1
      else:
          self.head = cur1
      temp = cur1.next
      cur1.next = cur2.next
      cur2.next = temp
  def find_node(self, data):
      prev = None
      cur = self.head
      while cur and cur.data!= data:
          prev = cur
          cur = cur.next
      return prev, cur
  def reverse(self):
      prev = None
      cur = self.head
      while cur:
          next = cur.next
          cur.next = prev
          prev = cur
          cur = next
      self.head = prev
  def merge_lists(self, head1, head2):
      if not head1:
          return head2
      if not head2:
          return head1
      temp = None
      if head1.data <= head2.data:
          temp = head1
          temp.next = self.merge_lists(head1.next, head2)
      else:
          temp = head2
          temp.next = self.merge_lists(head1, head2.next)
      return temp
  def reverse_k(self, head, k):
      prev = None
      cur = head
      next = None
      count = 0
      while cur and count < k:
          next = cur.next
          cur.next = prev
          prev = cur
          cur = next
          count += 1
      if next:
          head.next = self.reverse_k(next, k)
      return prev
  def detect_loop(self, head):
      mydict = {}
      if head:
          cur = head
          prev = None
          while cur and cur not in mydict:
              mydict[cur] = cur.data
              prev = cur
              cur = cur.next
          if cur in mydict:
              prev.next = None
              return True
      return False

  def sum_list(self, first, second):
      if first is None and second is None:
          return
      if first is None:
          return second
      if second is None:
          return first
      prev = None
      temp = None
      carry = 0
      while first is not None or second is not None:
          fdata = first.data if first is not None else 0
          sdata = second.data if second is not None else 0
          sum = carry + fdata + sdata
          carry = 1 if sum >= 10 else 0
          sum = sum if sum < 10 else sum%10
          temp = Node(sum)
          if self.head is None:
              self.head = temp
          else:
              prev.next = temp
          prev = temp
          if first is not None:
              first = first.next
          if second is not None:
              second = second.next
      if carry > 0:
          temp.next = Node(carry)

    def rotate(self, k):
        if self.head is None or k == 0:
            return
        cur = self.head
        count = 1
        while cur and count < k:
            cur = cur.next
            count += 1
        if cur is None:
            return
        knode = cur
        while cur.next:
            cur = cur.next
        cur.next = self.head
        self.head = knode.next
        knode.next = None
    def removeNthNodeFromEnd(self, head, n):
        if head:
            slow = fast = head
            for _ in range(n):
                fast = fast.next
            if not fast:
                return head.next
            while fast.next:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head

if __name__ == '__main__':
  llist = LinkedList()
  llist.push(20)
  llist.push(10)
  llist.append(40)
  llist.display()
  llist.insertAfter(llist.head.next, 30)
  llist.display()
  llist.delete(50)
  llist.display()
  llist.deleteAt(1)
  llist.display()
  len = llist.len()
  print(len)
  llist.display()
  llist.swap_nodes(30, 40)
  llist.display()
  llist.reverse()
  llist.display()
  llist1 = LinkedList()
  llist1.push(10)
  llist1.push(1)
  llist1.push(0)
  print('display first list')
  llist1.display()
  llist2 = LinkedList()
  llist2.push(100)
  llist2.push(10)
  llist2.push(3)
  print('display second list')
  llist2.display()
  llist3 = LinkedList()
  llist3.head = llist3.merge_lists(llist1.head, llist2.head)
  print('display sorted list')
  llist3.display()
  llist3.head = llist3.reverse_k(llist3.head, 4)
  llist3.display()
# # detect loop
  # node1 = Node(10)
  # node2 = Node(20)
  # node3 = Node(30)
  # node4 = Node(40)
  # node5 = Node(50)
  # llist = LinkedList()
  # llist.head = node1
  # node1.next = node2
  # node2.next = node3
  # node3.next = node4
  # node4.next = node5
  # node5.next = node2
  # print(llist.detect_loop(llist.head))
  # llist.display()
  # print(llist.detect_loop(llist.head))
# sum_list
# llist1 = LinkedList()
# llist1.push(3)
# llist1.push(2)
# llist1.push(1)
# llist1.display()
# llist2 = LinkedList()
# llist2.push(1)
# llist2.push(8)
# llist2.push(9)
# llist2.display()
# llist3 = LinkedList()
# llist3.sum_list(llist1.head, llist2.head)
# llist3.display()
# print('llist3')
# llist3.display()
# llist3.rotate(2)
# print('rotated llist3')
# llist3.display()
