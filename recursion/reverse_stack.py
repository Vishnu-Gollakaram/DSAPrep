class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        self.s = []

    def push(self, data):
        self.s.append(data)
        self.top = data
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Cannot Pop from an empty Stack")
        self.size -= 1
        if self.size == 0:
            self.top = None
        else:
            self.top = self.s[self.size - 1]
        return self.s.pop()
    
    def get_stack(self):
        return self.s
    
def reverse(stack):
    if stack.size <= 1:
        return
    
    last = stack.pop()
    reverse(stack)
    insert_first(stack, last)

def insert_first(stack, ele):
    if stack.size == 0:
        stack.push(ele)
        return

    last = stack.pop()
    insert_first(stack, ele)
    stack.push(last)

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(7)
stack.push(5)
stack.push(4)

print(stack.get_stack())
reverse(stack)
print(stack.get_stack())