class ArrayStack:

	def __init__(self):
		""" Creating an Empty Stack """
		self._data = []

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

	def pop():
		if self.isEmpty():
			print('Stack is EMPTY!')
		else:
			return self._data.pop()

