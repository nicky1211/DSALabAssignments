class ArrayStack:

	def __init__(self):
		""" Creating an Empty Stack """
		self._data = []
		self._revList = []

	def length(self):
		""" Return the length of the list """
		return len(self._data)

	def isEmpty(self):
		""" Check if the stack is empty """
		return len(self._data) == 0

	def push(self, e):
		""" Add an element on top of the stack """
		self._data.append(e)

	def top(self):
		if self.isEmpty():
			print('Stack is EMPTY!')
		else:
			return self._data[-1]

	def pop(self):
		""" Remove an element from top of the stack """
		if self.isEmpty():
			print('Stack is EMPTY!')
		else:
			return self._data.pop()

	def getData(self):
		return self._data

class ArrayQueue:
	""" FIFO queue implementation using a Python list as underlying storage """
	DEFAULTY_CAPACITY = 10

	def __init__ (self):
		""" Initialize the stacks """
		self._S1 = ArrayStack()
		self._S2 = ArrayStack()


	def len(self):
		""" Return the number of elements in the queue """
		return self._size

	def capacity(self):
		return len(self._data)

	def is_empty(self):
		""" Return True if the queue is empty """
		return self._size == 0

	def first(self):
		""" Return (not remove) the element at the fron of the queue
		"""
		if self.is_empty():
			print('Queue is empty')
		else:
			return self._data[self._front]

	def dequeuer(self):
		""" Remove and return the rear element of the queue		
		"""
		if self._S2.isEmpty():
			print("Empty")
		for i in range(self._S2.length()):
			self._S1.push(self._S2.pop())
			ele = self._S1.pop()
		for i in range(self._S1.length()):
			self._S2.push(self._S1.pop())
		return ele

	def dequeuef(self):
		""" Remove and return the front element of the queue		
		"""
		return self._S2.pop()

	def enqueuer(self, e):
		""" Add an element to the back of queue """
		if self._S2.length() == 0:
			self._S2.push(e)
		else:
			self._S1.push(self._S2.pop())
			self._S1.push(e)
			for i in range(self._S1.length()):
				self._S2.push(self._S1.pop())

	def enqueuef(self, e):
		""" Add an element to the front of queue """
		self._S2.push(e)


if __name__ == '__main__':
	Q = ArrayQueue()
	Q.enqueuef(10)
	Q.enqueuer(30)
	Q.enqueuef(40)
	Q.enqueuer(50)