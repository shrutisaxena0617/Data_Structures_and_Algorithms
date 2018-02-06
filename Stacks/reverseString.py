class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return (len(self.stack) == 0)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if(self.isEmpty()):
            return -1
        return(self.stack.pop())

    def display(self):
        for i in self.stack:
            print i,



# initialize stack object
stack = Stack()

# Function to reverse string
def reverseString(stack):
    result_str = []
    print('\n')
    while not stack.isEmpty():
        print stack.pop(),

# Input string from user and push in stack
print('Input string :: ')
user_input = raw_input()
for i in user_input:
    stack.push(i)

# Display original stringgt

stack.display()

# Reverse string

reverseString(stack)

#print stack.pop()

