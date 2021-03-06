

class SortedDictionary():

	"""
		class redifining dictionaries so they can be sorted and contains 
		more functionalities
	"""

	def __init__(self, base = {}, **keys_values):
		
		self._keys   = list(base.keys())
		self._values = list(base.values())
		#Checks if base is a valid dictionary or not
		if type(base) not in (dict, SortedDictionary):
			raise TypeError("{} is not a dictionary".format(base))	
		#we retrieve base's data
		for key in base:
			self[key] = base[key]		
		#retrieves data from keys_values
		for key,value in keys_values:
			self[key] = value

	def __getitem__(self, key):
		
		key = self._keys.index(key)	#we extract the index of 'index' in self.keys
		return self._values[key]	

	def __setitem__(self, key, value):
		
		if key not in self._keys:
		self._keys  .append(key)
			self._values.append(value)
		else:
			key = self._keys.index(key) #we extract the index of 'index' in self.keys
			self._values[key] = value	
			
	def __str__(self):

		return repr(self)

	def __repr__(self):
		
		first_passage = True
		string = "{"
		for key, value in self.items():
			if first_passage:
				string += repr(key) + ": " + repr(value) 
				first_passage = False
			else:
				string += "," + repr(key) + ": " + repr(value) 
		string += "}"

		return string

	def __iter__(self):
		
		return iter(self._keys)

	def items(self):
		
		for item in self._keys:
			yield (item, self._values[self._keys.index(item)])


	def add(self,dict_object ):
		""" Returns a new instance of SortedDictionary containing the concatenation of self and dict_object """
		if type(dict_object) is not type(self):
			raise TypeError("{} must be a  SortedDictionary".format(dict_object))
		
		new_SortedDictionary = SortedDictionary()
		for key in self:
			new_SortedDictionary[key] = self[key]	

		for key in dict_object:
			new_SortedDictionary[key] = dict_object[key]	
		return new_SortedDictionary;

	def contains(self, value):
		""" Returns True if self contains an element matching key """
		
		return value in self._values

	def sort(self):
		
		sorted_keys = sorted(self._keys)
		sorted_values = []
		#Updating the values according to sorted keys	
		for key in sorted_keys:
			value = self[key]
			sorted_values.append(value)
		#Updating keys and values with new sorted ones
		self._keys   = sorted_keys
		self._values = sorted_values	

		return list(self._keys)
	def values(self):
		""" returns a list keys of SortedDictionary """
		return list(self._values)

	def reverse(self):
		""" reverses the dictionary """
		rev_keys = []
		rev_values = []

		for key, value in self.items():
			rev_keys.insert(0, key)
			rev_values.insert(0, value)
		self._keys = rev_keys
		self._values = rev_values

	def delitem(self, key):
		""" Deletes a key in dictionary """
		if key not in self._keys:
			raise KeyError("{} is not in dictionary ".format(key))
		#Extracting key index 
		index = self._keys.index(key)
		
		#self._values.pop(index)
		#self._keys.pop(index)

		#To remove key we can also proceed like:
		del self._values[index]
		del self._keys[index]

	def len(self):
		""" returns the length of dictionary """

		return len(self._keys)

if __name__ == "__main__":


	di = {"khossan":1, "ishaq":2, "hibot":3}
	a = SortedDictionary(di)
	print(a)
	
	#a["khossan"] = 1
	#a["ishaq"]   = 2
	#a["hibot"]   = 3
	#print("a = {}".format(a))
	#a.sort()
	#print("sorted", a, sep= " >>> ")
	#a.reverse()
	#print("reversed", a, sep= " >>> ")
	#
	#a.delitem("ishaq")
	#print("after deleting a key ", a, sep= " >>> ")
	
	
