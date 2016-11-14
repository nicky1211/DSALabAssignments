class ArrayStack:

	def __init__(self):
		""" COnstructor to initialize the required datastructures, here 2 lists one for the data and the  """
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

	def transfer(self):
	    S1 = ArrayStack()
	    S2 = ArrayStack()
	    
	    sizeActual = len(self._data)

	    for x in range(sizeActual):
	    	S1.push(self.pop())
	    
	    for x in range(sizeActual):
	    	S2.push(S1.pop())
	    	
	    for x in range(sizeActual):
	    	self._data.append(S2.pop())

	    return self._data

if __name__ == '__main__':
	S = ArrayStack()
	temp1 = ArrayStack()
	S.push(5)
	S.push(10)
	lst = S.transfer()
	assert(lst == [10,5])