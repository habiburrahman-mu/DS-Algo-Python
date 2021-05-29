# list as stack
s = []
s.append(10)
s.append(12)
s.append(14)
print(s.pop())  # 14
print(s)  # [10, 12]

# deque as stack
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print(stack)  # deque(['a', 'b', 'c', 'd'])
print(stack.pop())  # d
print(stack)  # deque(['a', 'b', 'c'])

# Implementation using class
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        return self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):  # doesn't delete the value
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def __str__(self):
        return str(self.container)

s = Stack()
print(s.is_empty())  # True
s.push(100)
s.push(200)
s.push(300)
print(s.is_empty())  # False
print(s)  # deque([100, 200, 300])
s.pop()
print(s)  # deque([100, 200])
