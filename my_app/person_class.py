class Person(object):
	"""This class describes the instance of person
	"""
	def __init__(self,person_id, name):
		self.name = person_id
		self.name = name
		
class Fellow(Person):
	"""This class inherits from the Person class 
        and defines an instance of fellow 
	"""
	def __init__(self, person_id, name, wants_accom = "N"):
		super(Fellow, self).__init__(person_id, name)
		self.person_type = "Fellow"
		self.wants_accom = wants_accom	
		

class Staff(Person):
	"""This class inherits from the Person class 
        and defines an instance of Person
	"""
	def __init__(self, person_id, name):
		super(Staff, self).__init__(person_id, name)
		self.person_type = "Staff"
		
