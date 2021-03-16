
class Person:
	"""
		class defining a person overriding __new__ method
	"""
	def __new__(cls, name, age):
		
		print("__new__ method calling of class {}".format(cls))

		return object.__new__(cls)


	def __init__(self, name, age):
		
		print(" instance method __init__ calling ")
		self.name = name
		self.age = age

if __name__ == "__main__":
	
	person = Person("ishaq", 22)
	print("object after its creation")
	print("name ", person.name)
	print("age ", person.age)
