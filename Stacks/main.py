#Create stack
from Stacks.stack import Stack

print('Enter stack elements :: ')
empty_list = raw_input()
empty_list = empty_list.split()
stack = Stack()
for i in range(len(empty_list)):
    stack.push(int(empty_list[i]))

#Display stack
stack.display()

#Remove element from stack
pop = stack.pop()
print pop

stack.display()

