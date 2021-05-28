class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
            self.head = new_node

    def append(self, data):  # append to last
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def __str__(self):  # method overridden
        if self.head is None:
            return "List is Empty"
        else:
            st = ""
            cur = self.head
            while cur:
                st += str(cur.data) + " "
                cur = cur.next
                if cur is self.head:
                    break
            return st


if __name__ == "__main__":
    cLL = CircularLinkedList()
    cLL.prepend(100)
    cLL.prepend(200)
    cLL.append(10)
    print(cLL)  # 200 100 10
    cLL.append(20)
    cLL.append(30)
    cLL.append(40)
    print(cLL)  # 200 100 10 20 30 40
    cLL.prepend(200)
    print(cLL)  # 200 200 100 10 20 30 40 
