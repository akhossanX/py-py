

class Person:
	""" class modelizing a person """
	
	def __int__(self, name):
		self.name  = name
		self.lname = "abdo"

	def __str__(self):
		
		return "{} {} ".format(self.name, self.lname)

	def __setattr__(self, attr, value):
		
		object.__setattr__(self, attr, value)


class Agent(Person):
	""" agent is a person """

	def __init__(self, name):
		
		Person.__init__(self, name)
		self.matricule = 389828298

	
