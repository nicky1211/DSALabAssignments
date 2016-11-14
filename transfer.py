
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

	def pop(self):
		""" Remove an element from top of the stack """
		if self.isEmpty():
			print('Stack is EMPTY!')
		else:
			return self._data.pop()
    
	def transfer(self,s, t):
	    while(s.length()>0):
	        t.push(s.pop())

if __name__ == '__main__':
    s = ArrayStack()
    t = ArrayStack()
    for i in range(10):
        s.push(i)
    s.transfer(s, t)
    for i in range(10):
        print(t.pop())

		