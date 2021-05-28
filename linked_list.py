class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next
		return count

	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid index")
		if index == 0:
			self.head = self.head.next
			return
		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1

	def insert_at(self, index, data):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid Index")
		if index == 0:
			self.insert_at_beginning()
			return

		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				node = Node(data, itr.next)
				itr.next = node
				break

			itr = itr.next
			count += 1

	def print(self):
		if self.head is None:
			print("Linked list is empty")
			return

		itr = self.head
		listr = ''
		while itr:
			listr += str(itr.data) + " "
			itr = itr.next
		print(listr)


if __name__ == '__main__':
	ll = LinkedList()
	ll.insert_values(['A', 'B', 'C', 'D', 'E'])
	ll.insert_at_end('F')
	ll.insert_at_beginning('a')
	ll.print()  # a A B C D E F
	ll.remove_at(2)
	ll.print()  # a A C D E F
	ll.insert_at(3, 'Z')
	ll.print()  # a A C Z D E F
	ll.insert_at(3, 'X')
	ll.print() # a A C X Z D E F
	print("Length of linked list: ", ll.get_length())
	# Length of linked list:  8



