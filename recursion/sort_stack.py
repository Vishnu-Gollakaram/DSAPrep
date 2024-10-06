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

def sort(stack):
    if stack.size <= 1:
        return 
    last = stack.pop()
    sort(stack)
    insert(stack, last)

def insert(stack, ele):
    if stack.size == 0 or stack.top <= ele:
        stack.push(ele)
        return
    last = stack.pop()
    insert(stack, ele)
    stack.push(last)

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(7)
stack.push(5)
stack.push(4)

print(stack.get_stack())
sort(stack)
print(stack.get_stack())