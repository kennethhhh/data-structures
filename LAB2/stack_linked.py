class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Linked List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.head = None
        self.num_items=0

    def is_empty(self):
        """Returns True if the stack is empty, and False otherwise"""
        if self.num_items==0:
            return True
        else:
            return False

    def is_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if self.num_items==self.capacity:
            return True
        else:
            return False


    def push(self, item):
        """If stack is not full, pushes item on stack.
	    If stack is full when push is attempted, raises IndexError"""
        if self.is_empty():
            pushed_item=Node(item)
            pushed_item.next=self.head
            self.head=pushed_item
            self.num_items+=1
        elif self.is_full():
            raise IndexError
        else:
            pushed_item=Node(item)
            pushed_item.next=self.head
            self.head=pushed_item
            self.num_items+=1



    def pop(self): 
        """If stack is not empty, pops item from stack and returns item.
	    If stack is empty when pop is attempted, raises IndexError"""
        if self.is_empty():
            raise IndexError
        else:
            x=self.head
            new_head=self.head.next
            self.head=new_head
            self.num_items-=1
            return (x.data)

    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
	    If stack is empty, raises IndexError"""
        if self.is_empty():
            raise IndexError
        else:
            return (self.head.data)

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items

    def __repr__(self):
        return '{}, {}'.format(self.head.next.data,self.head.data)

 