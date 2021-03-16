

class RevStr(str):
	
	"""
		designed to reverse the iteration over an iterable
		when we use for to iterate over a str object, it starts from the last element and ends in the first element	
	"""

	def __iter__(self):

		return self

	def __init__(self, string):
		
		self.string = string
		self.position = len(string)
	
	def __next__(self):
		
		if self.position == 0:
			raise StopIteration
		self.position -= 1 #we decrement the position of iterator
		
		return self.string[self.position]


class ItRevStr:

	def __init__(self, string):
		
		self.string = string
		self.position = len(string)
	
	def __next__(self):
		
		if self.position == 0:
			raise StopIteration
		self.position -= 1 #we decrement the position of iterator
		
		return self.string[self.position]

