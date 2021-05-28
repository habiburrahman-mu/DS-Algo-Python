class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        st = ""
        cur = self.head
        while cur.next:
            st += str(cur.data) + " "
            cur = cur.next
        return st


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.prepend(10)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(5)
    print(dll.print_list())  # 10 1 2 3
    dll.prepend(9)
    dll.prepend(8)
    dll.prepend(7)
    print(dll.print_list())  # 7 8 9 10 1 2 3
