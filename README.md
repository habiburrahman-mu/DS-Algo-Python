# DS-Algo-Python
Implementation of different data structures and algorithms using Python

- - -

## Data Structures

### Array
*Python does not have built-in support for Arrays, but Python Lists can be used instead.*

- [array_.py](array_.py)

- - -

### Linked List
*A linked list is a sequence of data structures, which are connected together via links. Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array.*

- [linked_list.py](linked_list.py)

- - -

### Doubly Linked List
*Doubly linked list is a type of linked list in which each node apart from storing its data has two links. The first link points to the previous node in the list and the second link points to the next node in the list. The first node of the list has its previous link pointing to NULL similarly the last node of the list has its next node pointing to NULL.*

![Doubly Linked List](img/dll.jpg)

- [doubly_linked_list.py](doubly_linked_list.py)

- - -

### Circular Linked List
*Circular Linked List is a variation of Linked list in which the first element points to the last element and the last element points to the first element. Both Singly Linked List and Doubly Linked List can be made into a circular linked list.*

![Circular Linked List](img/singly_circular_linked_list.jpg)

- [circular_linked_list.py](circular_linked_list.py)

- - -

### Stack
*A stack is an Abstract Data Type (ADT), commonly used in most programming languages. It is named stack as it behaves like a real-world stack, for example – a deck of cards or a pile of plates, etc. Likewise, Stack ADT allows all data operations at one end only. At any given time, we can only access the top element of a stack. This feature makes it LIFO data structure. LIFO stands for Last-in-first-out. Here, the element which is placed (inserted or added) last, is accessed first. In stack terminology, insertion operation is called PUSH operation and removal operation is called POP operation*

<p align="center">
  <img src="img/stack.png">
</p>

- [stack_.py](stack_.py)
- [check_for_balanced_parentheses.py](check_for_balanced_parentheses.py)


- - -

### Queue
*A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.*

<p align="center">
  <img src="img/Queue.png">
</p>

- [queue_.py](queue_.py)
- [queue_list_deque.py](queue_list_deque.py)

- - -

## Searching Algorithms

### Linear Search

*Linear search or sequential search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched.*

- [linear_search.py](linear_search.py)

- - -

### Binary Search

*Binary Search is a searching algorithm for finding an element's position in a sorted array. In this approach, the element is always searched in the middle of a portion of an array. **Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.***

- [binary_search_iterative.py](binary_search_iterative.py)
- [Binary Search Implementation using Recursion](binary_search_recursive.py)

- - -