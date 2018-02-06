# Basic stack implementation

def createStack():
    my_stack = []
    return my_stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, elem):
    stack.append(elem)

def pop(stack):
    if(isEmpty(stack)):
        return -1
    return stack.pop()

#def top(stack):
    #write here

def display(stack):
    for i in range(len(stack)):
        print(stack[i])

stack = createStack()
print(isEmpty(stack))

#Create stack
print('Enter stack elements :: ')
empty_list = raw_input()
empty_list = empty_list.split()
for i in range(len(empty_list)):
    push(stack,int(empty_list[i]))

#Display stack
display(stack)

#Remove element from stack
pop = pop(stack)
print pop




