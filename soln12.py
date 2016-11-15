#Circularly array realization of queue
class ArrayQueue(object):
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        return self._data[self._front]
    
    def dequeue(self):
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)% len(self._data)
        self._size -= 1
        return answer
    
    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(self._data)
        self._front = 0
    
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def __repr__(self):
        return str(self._data)
        
    def rotate(self, d):
        for i in range(d):
            temp = self._data[self._front]
            avail = (self._size + self._front) % len(self._data)
            self._data[avail] = temp
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
        

class ArrayDeque(ArrayQueue):
    
    def __init__(self):
        super(ArrayDeque,self).__init__()
    
    def add_last(self,e):
        self.enqueue(e)
    
    def delete_first(self):
        return self.dequeue()
        
    def add_first(self,e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        
    def delete_last(self):
        back = (self._front + self._size -1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        return answer