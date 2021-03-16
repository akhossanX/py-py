import pickle

class Zdict:
	
	""" this class simulates a container class like dict() """
	
	def __init__(self):
		self._dictionary = {}
		self.name = "hello world"

	def __getitem__(self, item):
		return self._dictionary[item]

	def __setitem__(self, index, value):
		self._dictionary[index] = value

	def __contains__(self, item):
		""" checks if the iterable contains the item given as parameter """

		for elt in self._dictionary:
			if item ==  elt:
				return True
			else:
				return False

	def _get_dictionary(self):
		return self._dictionary

	def _set_dictionary(self, new_dictionary):
		self._dictionary = new_dictionary

	dictionary = property(_get_dictionary, _set_dictionary)

	def serialize(self):
		""" this method serializes an object , saves all its attributes """

		with open("serialized", "wb") as ser_object:
			pickler = pickle.Pickler(ser_object)
			pickler.dump(self)

	def deserialize(self):
		""" this method deserializes an object and saves all its attributes to 
			__dict__ attribute
		"""
		
		with open("serialized", "rb") as ser_object:
			unpickler = pickle.Unpickler(ser_object)
			self.__dict__ = unpickler.load().__dict__

	def __getstate__(self):
		""" before serializing sets the value of the first elt of dictionary to 'no description' """

		dict_attr = dict(self.__dict__)
		dict_attr["_dictionary"] = {"khossan": "no description"} 
		dict_attr["name"] = "abdelilah khossan"
		return dict_attr

	def __setstate__(self, dic_attr):
		
		""" called after the deserialization """
		dic_attr["name"] = "hibot"
		dic_attr["_dictionary"] = {"hibot": "friend"}
		self.__dict__ = dic_attr	



