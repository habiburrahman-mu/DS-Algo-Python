from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        return self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def __str__(self):
        return str(self.buffer)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())  # True
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    print(q)  # deque(['E', 'D', 'C', 'B', 'A'])
    print(q.dequeue())  # A
    print(q)  # deque(['E', 'D', 'C', 'B'])
    print(q.is_empty())  # False
    print(q.size())  # 4
