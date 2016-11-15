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
		if len(self._data) == self._restrictedLenght:
			self.leak(e)
		else:
			self._data.append(e)
			self._top +=1
		
	def leak(self,e):
		temp = ArrayStack()
		print (len(self._data) - 1)
		for i in range(len(self._data) - 1):
			temp.push(self._data.pop())
		# temp.displayData()
		self._data.pop()

		for each in temp.getData():
			self._data.append(temp.pop())

		self._data.append(e)
		self._top +=1


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

	def getData(self):
		return self._data

	def displayData(self):
		print self._data



def test_stack():
	size = 5
	st = ArrayStack(size)
	# st.displayData()
	st.push(10)
	st.push(20)
	st.push(30)
	st.push(40)
	st.push(50)	
	st.push(60)
	# st.displayData()
	# print "Adding the Extra element"
	#Adding the extra element will throw the exception
	# st.push(60)


if __name__ == '__main__':
	test_stack()