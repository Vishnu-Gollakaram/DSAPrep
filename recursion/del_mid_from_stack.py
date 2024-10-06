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

def del_mid(stack):
    if stack.size == 0:
        return
    mid =stack.size // 2 + 1
    helper(stack, mid)

def helper(stack, k):
    val = stack.pop()
    if k == 1:
        return
    helper(stack, k - 1)
    stack.push(val)

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(7)
stack.push(5)
stack.push(4)
stack.push(6)

print(stack.get_stack())
del_mid(stack)
print(stack.get_stack())