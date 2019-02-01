
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity=capacity
        self.items=[None]*capacity
        self.head=0
        self.rear=1
        self.num_items=0



    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items==0:
            return True
        return False



    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items==self.capacity:
            return True
        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise (IndexError)
        if self.is_empty():
            self.items[self.head]=item
            self.num_items+=1
        else:
            self.items[self.rear]=item
            #resets the rear to 0 if queue is not full and rear reached capacity
            self.rear= (self.rear+1)%self.capacity
            self.num_items+=1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise (IndexError)
        else:
            temp=self.items[self.head]
            #resets the head to 0 if queue is not full and head >capacity
            self.head=(self.head+1)%self.capacity
            self.num_items-=1
            #resets the head and rear
            if self.num_items==0:
                self.head=0
                self.rear=1
            return temp


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return (self.num_items)


