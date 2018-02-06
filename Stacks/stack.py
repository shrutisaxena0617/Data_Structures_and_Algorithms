class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if(self.isEmpty()):
            return -1
        return self.stack.pop()

    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])

