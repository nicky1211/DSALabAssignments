class ArrayQueue:
	""" FIFO queue implementation using a Python list as underlying storage """
	DEFAULTY_CAPACITY = 10

	def __init__ (self):
		""" create an empty queue """
		self._data = [None] * ArrayQueue.DEFAULTY_CAPACITY
		self._size = 0
		self._front = 0

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

	def dequeue(self):
		""" Remove and return the front element of the queue		
		"""

		if self.is_empty():
			print('Queue is empty')
		else:			
			answer = self._data[self._front]
			self._data[self._front] = None
			self._front = (self._front + 1) % len(self._data)
			self._size -= 1
			if 0 < self._size < len(self._data) // 4:
				self._resize(len(self._data) // 2)
			return answer

	def enqueue(self, e):
		""" Add an element to the back of queue """

		if self._size == len(self._data):				# if queue elements == queue capacity, allow queue capacity to grow 2* present capacity
			self._resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self._size += 1

	def _resize( self, cap):
		""" Resize to a new list of capacity >= len(self) """

		old = self._data
		self._data = [None] * cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0

class CapGain:

	def __init__(self):
		self._choice = 0
		self._totCapGain = 0
		self._shareHeld = ArrayQueue()
		self._priceOfShare = ArrayQueue()
		self._soldCount = []
		self._soldPrice = []
		self._buyCount = []
		self._buyPrice = []

	def menuPrompt(self):
		menu()
    	self._choice= int(input("Enter menu choice:\t"))
    	while self._choice != 4:
    		if self._choice == 1:
    			buyShare(numberOfShares,priceeach)
        	elif self._choice == 2:
        		shareSold,priceOfshareSold = sellShare()
            	print ("%s shares are sold for the price %s each"%(shareSold,priceOfshareSold))
        	elif self._choice == 3:
        		calCapGain()
       

	def menu(self):
		print("\n1 : Buy a Share\n2 : Sell the share\n3 : Total Capital Gain So far\n4 : Quit")
   	
   	def buyShare(self):
   		numberOfShares= int(input("Enter the number os Shares:\t"))
   		priceeach= int(input("Enter the price of each:\t"))
   		self._shareHeld.enqueue(numberOfShares)
   		self._priceOfShare.enqueue(priceeach)
   		self._buyCount.append(numberOfShares)
    	self._buyPrice.append(price)

    def sellShare(self):
    	shareSold = self._shareHeld.dequeue()
    	priceOfshareSold = self._priceOfShare.dequeue()
    	self._soldCount.append(shareSold)
    	self._soldPrice.append(priceOfshareSold)
    	return shareSold,priceOfshareSold

    def calCapGain(self):
    	totalBuyPrice = 0
    	totalBuyQuantity = 0
    	totalSellPrice = 0
    	totalSellQuantity = 0
    	spentWhileBuy = 0
    	amountafterSell = 0
    	captial = 0

    	for i,j in zip(self._buyCount,self._buyPrice)
    		totalBuyQuantity = totalBuyQuantity + i
    		totalBuyPrice = totalBuyPrice + j

    	spentWhileBuy = totalBuyQuantity * totalBuyPrice

    	for c,p in zip(self._soldCount,self._soldPrice)
    		totalSellQuantity = totalSellQuantity + c
    		totalSellPrice = totalSellPrice + p

    	amountafterSell = totalSellQuantity * totalSellPrice
    	capital = amountafterSell  - spentWhileBuy
    	if captial < 0:
    		print "You had a loss. The lost amount is %s"%abs(captial)
    	else:
    		print "You are under gain. The profit amount is %s"%captial


if __name__ == '__main__':
	transact = CapGain()

	transact.menuPrompt()


   