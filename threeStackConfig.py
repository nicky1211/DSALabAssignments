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
	def getData(self):
		return self._data


	def pop(self):
		""" Remove an element from top of the stack """
		if self.isEmpty():
			print('Stack is EMPTY!')
		else:
			return self._data.pop()

def test_concat():

	R = ArrayStack()
	S = ArrayStack()
	T = ArrayStack()

	R.push(1)
	R.push(2)
	R.push(3)
	assert(R.getData() == [1, 2, 3])
	
	S.push(4)
	S.push(5)
	sizeS = S.length()
	assert(S.getData() == [4,5])

	T.push(6)
	T.push(7)
	T.push(8)
	T.push(9)
	sizeT = T.length()
	assert(T.getData() == [6,7,8,9])

	for i in range(S.length()):
		T.push(S.pop())
	lst = T.getData()
	assert(lst == [6, 7, 8,  9, 5, 4])

if __name__ == '__main__':
	test_concat()