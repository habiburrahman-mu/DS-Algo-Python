# queue implementation using python list data structure
queue = []
queue.insert(0, 11)
queue.insert(0, 12)
queue.insert(0, 13)
print(queue)  # [13, 12, 11]
print(queue.pop())  # 11
print(queue)  # [13, 12]

# queue implementation using the collections.deque
from collections import deque
q = deque()
q.appendleft(10)
q.appendleft(100)
q.appendleft(1000)
print(q)  # deque([1000, 100, 10])
print(q.pop())  # 10