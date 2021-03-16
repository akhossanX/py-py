

class Test:
	"""
		this class is for testing
	"""

	def __init__(self):
		self.name = 'khossaan'
		self._age = 25

	def _get_age(self):
		return self._age
	
	def _set_age(self, new_age):
		self._age = new_age

	age = property(_get_age, _set_age)

	def __str__(self):
		return "{} is {} years old".format(self.name, self.age)

	def __setattr__(self, attr_name, attr_value):
		
		object.__setattr__(self, attr_name, attr_value)
		
	def __getattr__(self, attr_name):
		""" if attr_name does not exists Python executes this 
method """
		print(" no attribute called '{}' is defined 
here".format(attr_name))
		
	def __delattr__(self, attr_name):
		
		raise AttributeError("You can not delete any field in this 
class")


class Zdict:
	
	""" this class simulates a container class like dict() """
	
	def __init__(self):
		self._dictionary = {}

	def __getitem__(self, item):
		return self._dictionary[item]

	def __setitem__(self, index, value):
		self._dictionary[index] = value

	def __contains__(self, item):
		""" checks if the iterable contains the item given as 
parameter """

		for elt in self._dictionary:
			if item == elt:
				return True
			else:
				return False

	def _get_dictionary(self):
		return self._dictionary

	def _set_dictionary(self, new_dictionary):
		self._dictionary = new_dictionary

	dictionary = property(_get_dictionary,_set_dictionary)
