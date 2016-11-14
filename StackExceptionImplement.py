class Error(Exception):
   """Base class for other exceptions"""
   pass

class ArrayFullException(Error):
   """Raised when the input value is too small"""
   pass

class ArrayStack:
	""" LIFO stack implementation usinng Python list as underlying storage """
	def __init__ (self,MAX_LEN = 1):
		""" Creat an empty stack """
		self._restrictedLenght = MAX_LEN
		self._data = []
		self._top = -1
		self._size = 0

	def len (self):
		""" Return the number of elements in the stack """
		return len (self._data)
	
	def is_empty (self):
		""" Return True if the stack is empty """
		return len(self._data) == 0

	def push (self, e):
		try:
			if len(self._data) == self._restrictedLenght:
				raise ArrayFullException
			else:
				self._data.append(e)
				self._top +=1
		except ArrayFullException:
			print("The Max Size is reached!")
		
			

	def top (self):
		""" Return (but do not remove) the element at the top of the stack 

		"""
		if self.is_empty():
			print('Stack is empty')
		else:
			return self._data[-1]

	def pop (self):
		""" Remove and return the element from the top of the stack
		"""
		if self.is_empty():
			print('Stack is empty')			
		else:
			return self._data.pop()

	def display(self):
		print self._data



def test_stack():
	size = 5
	st = ArrayStack(size)
	st.push(10)
	st.push(20)
	st.push(30)
	st.push(40)
	st.push(50)	
	#Adding the extra element will throw the exception
	st.push(60)

if __name__ == '__main__':
	test_stack()