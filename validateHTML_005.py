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

def test_match_html(source):
	S = ArrayStack()
	j = source.find('<')

	while j != -1:
		l = source.find(' ', j+1)
		k = source.find('>', j+1)
		if k == -1:
			return False
		if l < k:
			tag = source[j+1 : l]
		else:
			tag = source[j+1 : k]
		if not tag.startswith('/'):
			S.push(tag)
		else:
			if S.isEmpty():
				return False
			if tag[1:] != S.pop():
				return False

		j = source.find('<',k+1)

	return S.isEmpty()

if __name__ == '__main__' :
	
	resultFalse = test_match_html('<html> <body <center> <h1> The little Boat </h1> </center> </body> </html>')
	assert(resultFalse == False)

	resultTrue = test_match_html('<html> <body> <center> <h1> The little Boat </h1> </center> </body> </html>')
	assert(resultTrue == True)
