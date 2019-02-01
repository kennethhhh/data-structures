class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    """A doubly-linked ordered list of integers, from lowest (head of list) to highest (tail of list)"""

    def __init__(self):
        """Use only a sentinel node
           ***No other instance variables***
           Do not have an attribute to keep track of size"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        """Returns back True if OrderedList is empty"""
        if self.sentinel.next==self.sentinel and self.sentinel.prev==self.sentinel:
            return True
        return False

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           Can assume that item is not already in list (no duplicate items)"""
        if self.is_empty():
            temp=Node(item)
            self.sentinel.next=temp
            self.sentinel.prev=temp
            temp.prev=self.sentinel
            temp.next=self.sentinel
        elif item>self.sentinel.prev.item:
            temp=Node(item)
            temp.prev=self.sentinel.prev
            temp.next=self.sentinel
            self.sentinel.prev.next=temp
            self.sentinel.prev=temp
        #figure out how to do middle numbers
        else:
            temp=Node(item)
            next_node=self.sentinel.next
            current_node=self.sentinel
            while item > next_node.item:
                next_node=next_node.next
                current_node=current_node.next
            next_node.prev=temp
            current_node.next=temp
            temp.next=next_node
            temp.prev=current_node


    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False"""
        next_node=self.sentinel.next
        current_node=self.sentinel

        if item > self.sentinel.prev.item or self.is_empty()==True:
            return False

        while item > next_node.item:
            next_node=next_node.next
            current_node=current_node.next

        if item==next_node.item:
            current_node.next=next_node.next
            next_node.next.prev=next_node.prev
            return True

        return False




    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None"""

        next_node=self.sentinel.next
        counter=0

        if item > self.sentinel.prev.item or self.is_empty()==True:
            return None
        #try:
        while item > next_node.item:
            next_node=next_node.next
            counter+=1
        #except:
            #pass

        if item==next_node.item:
            return counter
        return None

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError"""
        next_node=self.sentinel.next
        current_node=self.sentinel
        counter=0

        if index<0 or index>=self.size():
            raise IndexError


        while index != counter:
            next_node=next_node.next
            current_node=current_node.next
            counter+=1

        if counter==index:
            current_node.next=next_node.next
            next_node.next.prev=next_node.prev
            return next_node.item



    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list"""
        return (self.search_helper(self.sentinel.next,item))

    def search_helper(self,node, item):
        if node.item==item:
            return True
        if node==self.sentinel:
            return False
        return (self.search_helper(node.next,item))

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        python_list=[]
        next_node=self.sentinel.next
        while next_node.item!=None:
            python_list.append(next_node.item)
            next_node=next_node.next
        return python_list

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list"""
        return (self.python_list_reversed_helper(self.sentinel.next))

    def python_list_reversed_helper(self,node):
        if node==self.sentinel:
            return []
        return (self.python_list_reversed_helper(node.next)+[node.item])

    def size(self):
        """Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list"""
        return (self.size_helper(self.sentinel.next,0))

    def size_helper(self, node, count):
        if node == self.sentinel:
            return count
        return (self.size_helper(node.next, count+1))
