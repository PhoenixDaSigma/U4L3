class ArrayStack:
	
	def __init__(self):
		self.__stack = []
		self.__size = len(self.__stack)

	def __str__(self):
		"""Display contents of stack"""
		out = ""
		for ele in self.__stack:
			out += str(ele) + ' '
		
		out += "<TOP"
		return out

	def __len__(self):
		"""Returns the length of the stack"""
		return len(self.__stack)
	
	def push(self, thing):
		"""Adds an item to the top of the stack"""
		self.__stack.append(thing)
	
	def pop(self):
		"""Removes and returns the item on top of the stack"""
		empty = self.__isEmpty()
		if not empty:
			topItem = self.__stack[-1]
			del self.__stack[-1]
			return topItem
		else:
			raise IndexError("list assignment index out of range")
	
	def top(self):
		"""Returns the item on top of the stack"""
		empty = self.__isEmpty()
		if not empty:
			return self.__stack[-1]
		else:
			raise IndexError("list assignment index out of range")
	
	def __isEmpty(self):
		if len(self.__stack) > 0:
			return False
		else:
			return True