
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

	def reverse(self,S):
	    for x in range(S.length()):
	        self._revList.append(S.pop())
	    return self._revList



if __name__ == '__main__':
	S = ArrayStack()
	T = ArrayStack()
	#Add elements to the initial stack
	S.push(10)
	S.push(20)
	S.push(30)
	S.push(40)
	S.push(50)

	#Assert the length function
	assert(S.length() == 5)

	#Transfer the elements to generate a reverse list
	revList = S.reverse(S)

	#Assert the length of the new list
	assert(len(revList) == 5)

	#Assert if the new list has the elemenst in the rev order
	assert(revList == [50,40,30,20,10])
