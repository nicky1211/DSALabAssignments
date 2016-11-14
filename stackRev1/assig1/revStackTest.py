from ArrayStack import ArrayStack

def transfer(s,t):
   	t.push(s.pop())
    	
if __name__ == '__main__':
	

	# s1 = [10,20,30,40]
	# s2 = []
	# transfer(s1,s2)
	# assert(s2 == [40,30,20,10])

	s1 = ArrayStack()
	s1.push(10)
	s1.push(20)
	s1.push(30)
	#assert(length(s1) == 3)
	s2 = ArrayStack()
	transfer(s1,s2)
	print s1._data
	print s2._data